import pandas as pd
import jinja2
import os

def load_template(fn_template):
    path, filename = os.path.split(fn_template)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename)

def render_html(template, var, fn_html):
    html = template.render(var=var)
    with open(fn_html, 'w', encoding="UTF-8") as f:
        f.write(html)
    f.close()

class DataTable():
    def __init__(self, 
                 fn_template='template/datatables_template.html', 
                 html_title="Database Table"):
        self.template = load_template(fn_template)
        self.var = {"title": html_title}
    
    def render(self, dataframe, fn_html='datables.html'):
        self.output = fn_html
        self.var["head"] = list(df.columns)
        self.var["dataset"] = str(df.values.tolist())
        render_html(self.template, self.var, fn_html)

if __name__=="__main__":
    df = pd.read_csv("data.csv")
    dts = DataTable()
    dts.var["title"] = "test_table"
    dts.render(df)
    print(dts.output, "created!")
