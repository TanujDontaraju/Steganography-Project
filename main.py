

from bakery import assert_equal
from drafter import *
from dataclasses import dataclass

set_site_information(
    author="dtanuj@udel.edu",
    description="""A brief description of what your website does.
    Use a triple quoted string if you want to span multiple lines.""",
    sources=["N/A Right now but will add when I do"],
    planning=["Project_planning.pdf"],
    links=["https://github.com/UD-F25-CS1/cs1-website-f25-TanujDontaraju, Youtubelink""]
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
