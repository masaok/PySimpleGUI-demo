# https://stackoverflow.com/questions/57191494/draw-rectangle-on-image-in-pysimplegui

import PySimpleGUI as sg
import time

layout = [
    [
        sg.Graph(
            canvas_size=(400, 400),
            graph_bottom_left=(0, 0),
            graph_top_right=(400, 400),
            key="graph"
        )
    ]
]

window = sg.Window("rect on image", layout)
window.Finalize()

graph = window.Element("graph")

# graph.DrawImage(filename="foo.png", location=(0, 400))
graph.DrawRectangle((200, 200), (250, 300), line_color="blue")
graph.draw_rectangle((201, 201), (250, 300), line_color="red")
graph.draw_rectangle((250, 250), (300, 300), fill_color="yellow")

# draw_circle(center_location,
#     radius,
#     fill_color = None,
#     line_color = "black",
#     line_width = 1)
graph.draw_circle((100, 200), 10, fill_color="green")  # top left
graph.draw_circle((200, 200), 10, fill_color="red")    # top right
graph.draw_circle((200, 100), 10, fill_color="blue")   # bottom right
graph.draw_circle((100, 100), 10, fill_color="yellow")  # bottom left

# draw_text(text,
#     location,
#     color = "black",
#     font = None,
#     angle = 0,
#     text_location = "center")
graph.draw_text("hello",
                (50, 50),
                color="black",
                font=None,
                angle=0,
                text_location="center")

while True:

    epoch_time = int(time.time())
    graph = window.Element("graph")

    print("TIME:" + str(epoch_time))

    graph.draw_text(epoch_time,
                    (100, 50),
                    color="black",
                    font=None,
                    angle=0,
                    text_location="center")

    event, values = window.Read(timeout=1000)
    # event, values = window.Refresh()  # locks up

    if event is None:
        break
