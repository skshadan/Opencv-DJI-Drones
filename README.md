![App Screenshot](https://raw.githubusercontent.com/skshadan/Opencv-DJI-Drones/main/images/Slide%2016_9%20-%201.png)
# OpenCV with DJI Drones
So, you're trying to tap into your DJI drone's camera feed to use OpenCV, huh? Doesn't matter if it's a DJI Mini 2, DJI Mini 2 SE, or some other model, it can be a real pain, right? I was in the same boat, but after messing around with a bunch of methods, I finally cracked it.


## Step 1 Create an RTMP Server

- (Note: I used AWS EC2)

- What is RTMP Server?

An RTMP Server is a type of server that uses the Real Time Messaging Protocol (RTMP). This protocol, developed by Adobe Systems, is primarily used for streaming audio, video, and data over the internet. When you create an RTMP Server, you essentially set up a destination for your stream, which can then be accessed and viewed by others on the internet.

## Step 2 Add Security Groups

- Use this Security Group to enable both inbound and outbound traffic.

- Inbound Rules
![App Screenshot](https://raw.githubusercontent.com/skshadan/Opencv-DJI-Drones/main/images/inbound.png)

- Outbound Rules
![App Screenshot](https://raw.githubusercontent.com/skshadan/Opencv-DJI-Drones/main/images/outbound.png)
# Step 3: Connect with Your Server
```bash
sudo apt update && sudo apt upgrade -y
```
```bash
sudo apt install nginx
```
```bash
sudo add-apt-repository universe
```
```bash
sudo add-apt-repository universe
```
```bash
sudo apt install libnginx-mod-rtmp
```
```bash
sudo nano /etc/nginx/nginx.conf  or   search for "etc/nginx/nginx.conf"  with "Win SCP"

Modify NGINX configuration and save (scroll to the bottom of the .conf file and add the following code)
```
```bash
rtmp {

  server {

    listen 1935;

    chunk_size 4096;


    application live {

      live on;

      record off;

    }

  }

}

```
```bash
sudo systemctl restart nginx
```








## Screenshots
Open the DJI Fly App ⇒ Connect your drone ⇒ Navigate to 'Transmission' ⇒ Click on 'Live Streaming Platforms'. Here, you'll find the RTMP option. Enter your server IP address as shown.

![App Screenshot](https://raw.githubusercontent.com/skshadan/Opencv-DJI-Drones/main/images/IMG_5319.png)

## Example Code to Access the Video Feed
And boom! That's all it takes to tap into your DJI Drone Camera Feed from anywhere with RTMP. Stuck or got a question?
just hit me up.

![App Screenshot](https://raw.githubusercontent.com/skshadan/Opencv-DJI-Drones/main/images/code.png)
