from jinja2 import Template,Environment
# from urllib.request import urlopen
import urllib.request
from sys import argv
from json import loads
from os.path import isfile,isdir
from subprocess import call
from datetime import datetime
import click


paper_list_template_latex = Template(r'''\section*{PUBLICATIONS}
%% \vspace{-.3cm}

\begin{longtable}{c p{\rtcolw}}
{% for paper in papers %}
%% \multirow{3}{*}
\parbox[c]{1.9cm}{ \href{ {{- paper.titlelink -}} }{\includegraphics[width=1.8cm]{figures/{{ paper.image -}} }} }
& \parbox[c]{\rtcolw}{\textbf{ {{- loop.revindex }}. {{ paper.title -}} }  \hfill {{ paper.year }} \\ {% for author in paper.author %} {{ author.fullname }}{% if not loop.last %},{% endif %} {% endfor -%} } \\
{% endfor %}
 \end{longtable}
''')

paper_list_template_markdown = Template(r'''Title: Publications

<div>
{% for paper in papers %}
<p>{{- loop.revindex }}. <a href="{{- paper.titlelink -}}">{{ paper.title -}}</a>, {{ paper.year }}. {% for author in paper.author %}{{ author.fullname }}{% if not loop.last %}, {% else %}.{% endif %}{% endfor %}</p>
{% endfor %}
</div>
''')

press_list_template_latex = Template(r'''\section*{PRESS}
%% \vspace{-.3cm}

\begin{longtable}{c p{\rtcolw}}
{% for press in press_all %}
%% \multirow{3}{*}
\parbox[c]{1.1cm}{ \href{ {{- press.url -}} }{\includegraphics[width=1.1cm]{figures/{{ press.image -}} }} }
& \parbox[c]{\rtcolw}{ {\small \textcolor{blue}{\textit{\href{ {{- press.title -}} } { {{- press.title -}} } } } }\\ \textbf{ {{- press.organization -}} }, {{ press.date }} }\\
{% endfor %}
 \end{longtable}
''')

press_list_template_latex_two_rows = Template(r'''\section*{PRESS}
%% \vspace{-.3cm}

\begin{longtable}{c p{7.5cm} c p{7.5cm} }
{% for press in press_all %}
\parbox[c]{1.1cm}{ \href{ {{- press.url -}} }{\includegraphics[width=1.1cm]{figures/{{ press.image -}} }} }
& \parbox[c]{7.5cm}{ {\small \textcolor{blue}{\textit{\href{ {{- press.url -}} } { {{- press.title -}} } } } }\\ \textbf{ {{- press.organization -}} }, {{ press.formatted_date }} } {% if loop.index is divisibleby(2) %} \\
\rule{0pt}{5ex}{% else %} & {% endif %} {% endfor %}
 \end{longtable}
''')


@click.command()
@click.argument("username")
@click.argument("image_dir")
@click.argument("press_or_paper")
@click.argument("output_file")
def main(username, image_dir, press_or_paper, output_file):
    endpoint = urllib.request.Request("http://vermontcomplexsystems.org/api/v1/person/?format=json&uname={}".format(username))
    result_raw = urllib.request.urlopen(endpoint).read().decode('utf-8')
    result_json = loads(result_raw)
    for result in result_json["objects"]:
        print("found user {}".format(result["fullname"]))
        print("using the first user result")

    my_result = result_json["objects"][0]

    if press_or_paper == "papers":
        for paper in my_result["papers"]:
            print("found paper {}".format(paper["title"]))
            # save the figures
            image_link = "http://cmplxsys.w3.uvm.edu{}".format(paper["image"])
            print(image_link)
            image_filename = list(image_link.split("/")[-1].replace(" ","-").replace("%20","-").replace(".","-"))
            image_filename[-4] = "."
            image_filename = "".join(image_filename)
            if not isfile(image_dir+"/"+image_filename):
                f = open(image_dir+"/"+image_filename,"wb")
                f.write(urllib.request.urlopen(image_link).read())
                f.close()
            paper["image"] = image_filename
            max_authors = 5
            if len(paper["author"]) > max_authors:
                paper["author"] = paper["author"][:(max_authors+1)]
                paper["author"][max_authors] = {"fullname": "et. al"}

        # render and save the template
        # print(paper_list_template.render(my_result))
        f = open(output_file,"w")
        f.write(paper_list_template_markdown.render(my_result))
        f.close()

    if press_or_paper == "press":
        for press in my_result["press_all"]:
            print("found press {}".format(press["title"]))
            # save the figures
            image_link = "http://cmplxsys.w3.uvm.edu{}".format(press["image"])
            print(image_link)
            image_filename = list(image_link.split("/")[-1].replace(" ","-").replace("%20","-").replace(".","-"))
            image_filename[-4] = "."
            image_filename = "".join(image_filename)
            if not isfile(image_dir+"/"+image_filename):
                f = open(image_dir+"/"+image_filename,"wb")
                f.write(urllib.request.urlopen(image_link).read())
                f.close()
            press["image"] = image_filename
            press["title"] = press["title"].replace("&","\&")
            press["date"] = datetime.strptime(press["date"],"%Y-%m-%dT%H:%M:%S")
            press["formatted_date"] = press["date"].strftime("%B %-d, %Y")

        # render and save the template
        f = open(output_file,"w")
        f.write(press_list_template_latex_two_rows.render(my_result))
        f.close()

    # # render the pdf to see the result
    # call("pdflatex andrew-reagan-cv",shell=True)
    # call("open andrew-reagan-cv.pdf",shell=True)

if __name__ == "__main__":
    main()
