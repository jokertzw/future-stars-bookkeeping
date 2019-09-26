import pandas as pd

account = pd.read_csv('account-for-test.csv')

balance = 0
trs = ""

for i in account.iterrows():
    balance += i[1][2]
    trs += """
    <tr>
        <th scope="row">{}</th>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>""".format(i[0], i[1][0], i[1][1], i[1][2], i[1][3], i[1][4], balance)

html_report_template = open("template.html", "r", encoding='UTF-8').read()
open("report.html", "w", encoding='UTF-8').write(html_report_template.format(trs=trs))
