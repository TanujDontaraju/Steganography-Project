from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

set_site_information(
    author="your_email@udel.edu",
    description="""A brief description of what your website does.
    Use a triple quoted string if you want to span multiple lines.""",
    sources=["List any help resources or sources you used"],
    planning=["your_planning_document.pdf"],
    links=["https://github.com/your-username/your-repo"]
)
hide_debug_information()
set_website_title("Your Website Title")
set_website_framed(False)

hide_debug_information()
set_website_title("Your Drafter Website")
set_website_framed(False)


@dataclass
class State:
    pass


@route
def index(state: State) -> Page:
    return Page(state, ["Hello World!"])

assert_equal(index(State()), Page(State(), ["Hello World!"]))

start_server(State())
