/* sound.c
 *
 * Copyright (C) 2001-2006  Jonathan Blandford <jrb@alum.mit.edu>
 * Copyright (C) 2008 Cosimo Cecchi <cosimoc@gnome.org>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public
 * License along with this program; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 */

#include <gtk/gtk.h>
#include <canberra-gtk.h>

void
screenshot_play_sound_effect (const gchar *event_id,
                              const gchar *event_desc)
{
  ca_context *c;
  ca_proplist *p = NULL;
  int res;

  c = ca_gtk_context_get ();

  res = ca_proplist_create (&p);
  if (res < 0)
    goto done;

  res = ca_proplist_sets (p, CA_PROP_EVENT_ID, event_id);
  if (res < 0)
    goto done;

  res = ca_proplist_sets (p, CA_PROP_EVENT_DESCRIPTION, event_desc);
  if (res < 0)
    goto done;

  res = ca_proplist_sets (p, CA_PROP_CANBERRA_CACHE_CONTROL, "permanent");
  if (res < 0)
    goto done;

  ca_context_play_full (c, 0, p, NULL, NULL);

 done:
  if (p != NULL)
    ca_proplist_destroy (p);

}
