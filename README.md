# Triller-View-Bot
Asynchronous view bot for Triller.

## Information
This tool was strictly developed to demonstrate how straightforward it is to develop a view bot for services like Triller. I sent 1 million views to my video in a matter of minutes, and that resulted in hundreds of legitimate followers and likes — looks like my video got to the trending page. Please refrain from using this bot as it was once again developed for educational purposes only. Nevertheless, if you use this, you are doing it at your own risk. You have been warned.

I developed a multi-threadaed version before this one, but figured it had to be inefficient (one thread can handle way more requests than 1, so why stick to 1?) so I developed an asynchronous version. I compared the two different versions, and got some interesting results.

**Multi-threaded version:**
- Views sent: 10.000
- Time elapsed (hh:mm:ss): 00:00:49
- CPU usage: 74%

**Asynchronous version:**
- Views sent: 10.000
- Time elapsed (hh:mm:ss): 00:00:22
- CPU usage: 9%

## Preview
![](https://i.imgur.com/PnfvxCA.gif)<br>
![](https://i.imgur.com/1cxcJxy.png)

## Usage
- Python 3.6 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.

Run the following command to install the required dependencies; make sure PIP is added to PATH.
```
pip3 install aiohttp==3.6.2
```
1. Run main.py.
2. Enter the amount of views you would like to be added.
3. Paste the video's ID and hit enter — to find the ID, you have to reverse Triller's mobile API and monitor the like, report or comment request on the specific video (there are of course more endpoints that reveal the video's ID, but these are some of them). First you have to bypass SSL pinning though, because they do not trust all SSL certificates.

## Legal Notice
This is illegal if you use it without the consent of the creators — in this case, the Triller team. I am not accountable for any of your actions; this was merely a speedrun to demonstrate how view bots work. Please do not misuse this tool.
