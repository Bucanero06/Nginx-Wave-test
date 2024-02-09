# Copyright (c) 2024 Carbonyl LLC & Carbonyl R&D
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import asyncio
import os

import dotenv
from h2o_wave import main, Q, app, ui, on, data, run_on  # noqa F401

dotenv.load_dotenv(dotenv.find_dotenv())






async def on_startup():
    print("Startup event triggered")


async def on_shutdown():
    print("Shutdown event triggered")


@on('@system.client_disconnect')
async def on_client_disconnect(q: Q):
    print('Client disconnected')




async def init(q: Q) -> None:
    """
    Q Page Meta (meta_card) Arguments:
        box
            A string indicating how to place this component on the page.
        title
            The title of the page.
        refresh
            Refresh rate in seconds. A value of 0 turns off live-updates. Values != 0 are currently ignored (reserved for future use).
        notification
            Display a desktop notification.
        notification_bar
            Display an in-app notification bar.
        redirect
            Redirect the page to a new URL.
        icon
            Shortcut icon path. Preferably a .png file (.ico files may not work in mobile browsers). Not supported in Safari.
        layouts
            The layouts supported by this page.
        dialog
            Display a dialog on the page.
        side_panel
            Display a side panel on the page.
        theme
            Specify the name of the theme (color scheme) to use on this page. One of 'light', 'neon' or 'h2o-dark'.
        themes
            Themes (color schemes) that define color used in the app.
        tracker
            Configure a tracker for the page (for web analytics).
        scripts
            External Javascript files to load into the page.
        script
            Javascript code to execute on this page.
        stylesheet
            CSS stylesheet to be applied to this page.
        stylesheets
            External CSS files to load into the page.
        commands
            Contextual menu commands for this component.
    """
    # Static Business Website
    # index_file = open('static/html/index.html', 'r').read()

    q.page['meta'] = ui.meta_card(box='',
                                  title='AntBot',
                                  layouts=[ui.layout(breakpoint='xs', min_height='100vh', name='default',
                                                     zones=[
                                      ui.zone('main', size='1', direction=ui.ZoneDirection.ROW, zones=[
                                          ui.zone('sidebar', size='180px'),
                                          ui.zone('body', zones=[
                                              ui.zone('header'),
                                              ui.zone('content', zones=[
                                                  # Specify various zones and use the one that is currently needed. Empty zones are ignored.
                                                  ui.zone('first_context', size='0 0 1 4',
                                                          direction=ui.ZoneDirection.ROW,
                                                          zones=[
                                                              ui.zone('first_context_1', size='1 4 0 0'),
                                                              ui.zone('first_context_2', size='1 4 0 0'),
                                                              ui.zone('first_context_3', size='1 4 0 0'),
                                                              ui.zone('first_context_4', size='1 4 0 0'),
                                                          ]),
                                                  ui.zone('second_context', size='0 0 1 4',
                                                          direction=ui.ZoneDirection.ROW,
                                                          zones=[
                                                              ui.zone('second_context_1', size='1 4 0 0'),
                                                              ui.zone('second_context_2', size='1 4 0 0'),
                                                              ui.zone('second_context_3', size='1 4 0 0',
                                                                      direction=ui.ZoneDirection.ROW,
                                                                      zones=[
                                                                          ui.zone('second_context_3_1', size='1 4 0 0'),
                                                                          ui.zone('second_context_3_2', size='1 4 0 0')
                                                                      ]),
                                                          ]),
                                                  ui.zone('details', size='4 4 4 4'),
                                                  ui.zone('horizontal', size='1', direction=ui.ZoneDirection.ROW),
                                                  ui.zone('centered', size='1 1 1 1', align='center'),
                                                  ui.zone('vertical', size='1'),
                                                  # Wrapping = 'start', 'end', 'center', 'between', 'around', 'stretch'
                                                  # Layout = 'start', 'end', 'center', 'between', 'around'
                                                  ui.zone('grid_1', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='center'),
                                                  ui.zone('grid_2', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='start'),
                                                  ui.zone('grid_3', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='center'),
                                                  ui.zone('grid_4', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='center'),
                                                  ui.zone('grid_5', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='center'),
                                                  ui.zone('grid_6', direction=ui.ZoneDirection.ROW, wrap='stretch',
                                                          justify='center'),
                                                  ui.zone('bot_manual_controls',
                                                            direction=ui.ZoneDirection.ROW,
                                                          # Cover the entire card
                                                            wrap='stretch',

                                                            ),
                                              ]),
                                          ]),
                                      ]),
                                      ui.zone('footer', size='0 1 0 0', direction=ui.ZoneDirection.ROW),
                                  ]),
                                           ],
                                  themes=[
                                      ui.theme(
                                          name='my-awesome-theme',
                                          primary='#8C1B11',  # Header and Sidebaer - Color Light Red
                                          text='#000000',  #
                                          card='#ffffff',
                                          page='#F2F2F2',
                                          # page='#D91A1A',

                                      ),
                                      ui.theme(
                                          name='my-awesome-theme1',
                                          primary='#571305',  # Header and Sidebaer - Color Light Red
                                          text='#E0E0E0',  #
                                          card='#333333',
                                          page='#121212',

                                      ),
                                      ui.theme(
                                          name='my-awesome-theme2',
                                          primary='#2979FF',  # Header and Sidebaer - Color Light Red
                                          text='#E0E0E0',  #
                                          card='#212121',
                                          page='#000000',

                                      )
                                  ],
                                  theme='my-awesome-theme2'
                                  )

    q.client.initialized = False


async def render_login_page(q: Q, error_message=None):
    """Render the login page."""

    items = [
        ui.message_bar(type='info', text='Please login to continue.', ),
        ui.text_xl('Login'),
        ui.textbox(name='email', label='Email', required=True),
        ui.textbox(name='password', label='Password', required=True, password=True),
        ui.buttons([ui.button(name='login', label='Login', primary=True, )]),
    ]
    if error_message:
        items.insert(0, ui.message_bar(type='error', text=error_message))

    q.page['login'] = ui.form_card(box='centered', items=items)





@app('/', on_startup=on_startup, on_shutdown=on_shutdown)
async def serve(q: Q):
    """Main application handler."""
    print("Serving")
    if not q.client.initialized:
        print("Initializing")
        await init(q)
        q.client.initialized = True

    # Render something doesnt matter what
    await render_login_page(q)

    await q.page.save()
    print("Served")
