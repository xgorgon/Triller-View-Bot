from aiohttp import ClientSession
import asyncio
import os
import random
import threading
from time import time, strftime, gmtime, sleep


class ViewBot:
    def __init__(self):
        self.sent = 0
        self.retries = 0

    async def _task(self, session, video_id):
        auth_token = ''.join(random.choice(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
        ) for _ in range(43))
        error = False

        try:
            async with session.post(
                'https://social.triller.co/v1.5/api/videos/play', json={
                    'auth_token': (
                        'eyJhbGciOiJIUzI1NiIsImlhdCI6MTYwMTcyMDc4OSwiZXhwIjoxNjUzNTYwNzg5fQ.eyJpZCI'
                        f'6IjI0MDQ4NzUwMiJ9.{auth_token}'
                    ),
                    'sound_active': True,
                    'video_id': video_id
                }
            ) as response:
                data = await response.json()
        except Exception:
            error = True
        else:
            if data['status']:
                self.sent += 1
            else:
                error = True

        if error:
            self.retries += 1
            await self._task(session, video_id)

    def _title_updater(self, views_amount):
        # Avoid ZeroDivisionError.
        while not self.sent:
            sleep(0.1)
        start_time = time()

        while self.sent < views_amount:
            elapsed = time() - start_time

            # (Elapsed Time / Sent) * Remaining
            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    elapsed / self.sent * (views_amount - self.sent)
                )
            )

            time_elapsed = strftime('%H:%M:%S', gmtime(elapsed))
            os.system(
                f'title [Triller View bot] - Sent: {self.sent} ('
                f'{round(((self.sent / views_amount) * 100), 3)}%) ^| Retries: {self.retries} ^| Ti'
                f'me Elapsed: {time_elapsed} ^| Time Remaining: {time_remaining}'
            )
            sleep(0.1)

        print('\n[!] All views sent.')
        os.system(
            f'title [Triller View bot] - Sent: {self.sent} ('
            f'{round(((self.sent / views_amount) * 100), 3)}%) ^| Retries: {self.retries} ^| Time E'
            f'lapsed: {time_elapsed} ^| Time Remaining: 00:00:00 && pause >NUL'
        )

    async def main(self, amount, id):
        threading.Thread(target=self._title_updater, args=(amount,)).start()

        async with ClientSession(headers={
            'Host': 'social.triller.co',
            'Content-Type': 'application/json',
            'Connection': 'keep-alive',
            'Signature': 'XcMnVSMgbfnGlxXf783hbIVn47fhrCKDOxAdvF1GNPQ=',
            'Accept': '/',
            'User-Agent': 'Triller/14.4 (iPhone; iOS 13.7; Scale/3.00)',
            'Accept-Language': 'sv-SE;q=1, en-US;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
        }) as s:
            await asyncio.gather(*[self._task(s, id) for _ in range(amount)])

        # Prevents event loop from closing before aiohttp's session closes itself.
        await asyncio.sleep(1)


if __name__ == '__main__':
    os.system('cls && title [Triller View bot]')
    try:
        views_amount = int(input('[>] Amount of views to send: '))
    except ValueError:
        print('[!] Integer expected.')
        os.system('pause >NUL')
    else:
        try:
            video_id = int(input('[>] Video ID: '))
        except ValueError:
            print('[!] Invalid Video ID.')
            os.system('pause >NUL')
        else:
            view_bot = ViewBot()
            asyncio.run(view_bot.main(views_amount, video_id))
