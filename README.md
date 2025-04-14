Got the Tools: We used two cool pieces of software:

Prometheus: This is like our data collector. It goes to our app, asks for its "health stats" (like how many requests it's getting and how much memory it's using), and remembers them.
Grafana: This is like our dashboard. It takes the data Prometheus collected and shows it to us in easy-to-understand charts and graphs.
Put Them in Containers (Using Docker): To keep things tidy and easy to manage, we packed Prometheus and Grafana into little virtual boxes called "containers" using a tool called Docker. This makes sure they have everything they need to run without messing up anything else on our computer.

Told Prometheus Where to Look: We gave Prometheus instructions on where to find our app's health stats (it's at a special web address our app provides).

Connected Grafana to Prometheus: We then told Grafana how to talk to Prometheus so it could get the data.

Made a Simple Graph: We created a basic chart in Grafana to see how many requests our app was getting over time. This helps us see if traffic is going up or down.

Set Up a Basic Alarm: Finally, we set up a simple alarm in Grafana. If our app suddenly stops getting any requests for a little while, Grafana will send us a notification. This could mean something important is wrong!
