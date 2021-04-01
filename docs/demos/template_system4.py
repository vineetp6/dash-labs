import dash_labs as dl
import dash

app = dash.Dash(__name__, plugins=[dl.Plugin()])
tpl = dl.templates.DbcCard(title="Simple App", columns=6)


@app.callback(
    tpl.button_input("Click Me", label="Button to click"),
    template=tpl,
)
def callback(n_clicks):
    return "Clicked {} times".format(n_clicks)


app.layout = tpl.layout(app)

if __name__ == "__main__":
    app.run_server(debug=True)