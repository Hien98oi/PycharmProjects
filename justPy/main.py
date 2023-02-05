import justpy as jp


@jp.SetRoute("/")
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-4")
    in_1 = jp.Input(a=wp,
             placeholder="Enter first value",
             classes="form-input")
    in_2 = jp.Input(a=wp,
             placeholder="Enter second value",
             classes="form-input")
    d_output = jp.Div(a=div1, text="Result goes here...!",
           classes="text-gray-600")
    jp.Div(a=div1, text="Just another div...",
           classes="text-gray-600")
    jp.Div(a=div1, text="Yet another div",
           classes="text-gray-600")
    div2 = jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=wp,
              text="Calculate",
              click = sum_up, in1=in_1, in2=in_2,
              d = d_output,
              classes="border-border-blue-500 m-12 py-1 px-4 rounded " 
                      "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="I am cool interactive div")
    return wp

def sum_up(widget, msg):
    print(widget.in1.value, widget.in2.value)


@jp.SetRoute("/")
def about():
    wp = jp.WebPage()
    jp.Div(a=wp, text="Hi world")
    jp.Div(a=wp, text="Hi again!")
    return wp


# jp.Route("/", home)

jp.justpy()
