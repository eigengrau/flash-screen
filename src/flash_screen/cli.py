"""The flash-screen command-line interface."""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from flash_screen.flash import Flash


def console_entry():

    Flash()
    Gtk.main()
