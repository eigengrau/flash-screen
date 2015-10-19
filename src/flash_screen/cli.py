"""The flash-screen command-line interface."""

import argparse

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from flash_screen.flash import Flash


parser = argparse.ArgumentParser(
    description="Make the screen flash."
)

parser.add_argument(
    "--muted",
    dest='muted',
    default=False,
    action='store_true',
    help="Mute the shutter sound."
)


def console_entry():

    args = parser.parse_args()
    Flash(sound=not args.muted)
    Gtk.main()
