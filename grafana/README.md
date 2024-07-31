## Install Grafana
### Install Grafana on Windows
1. Go to [Grafana Install Page](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

2. Click on `Windows`

3. Navigate to Grafana download page

4. Choose `OSS` under edition for open source

5. Download and run installer choosing all default options

6. Navigate to C:\\'Program Files'\GrafanaLabs\grafana\bin

7. Run `grafana-server` application

8. Now open `localhost:3000` in a browser

9. Type in `admin` for username and password

10. Update password

### Install Grafana on Other Platforms
1. Go to [Grafana Install Page](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

2. Find your platform and click link to tutorial for grafana installation

3. Follow tutorial and make sure to choose Grafana OSS edition

4. After install open `localhost:3000` in a browser

5. Enter `admin` for both username and password

6. Update password

## Set up Database Connection
1. Open menu using the hamburger button in the top left corner of Grafana

2. Go to Connections drop down and choose `Data Sources`

3. Click on `Add new data source` and choose MySQL

4. Choose a name for the new Data Source

5. Under `Connection` enter the IP address of the database in `Host URL` and name of the databse in `Database name`

6. Under `Authentication` enter your username and password chosen when setting up the database

7. Scroll all the way down and click on `Save & test` to verify database is accessible

## Set up Dashboard
1. Open menu using the hamburger button in the top left corner of Grafana

2. Go to `Dashboards`

3. Click on `New` drop down menu in the top right corner and choose `Import`

4. Upload JSON file found in grafana folder on Github

5. Now we can update the Dashboard name if needed

6. Scroll down to `Select a MySQL data source` and choose your new Data Source

7. Scroll down to the bottom and click `Import`

## Tips for using the Dashboard
* In the top right corner there is an arrow pointing up that can be clicked to hide the topmost bar
* To the left of the arrow is an icon called kiosk mode which will hide all clutter above the dashboard
  * Enter ESC to get out of kiosk mode
* To the left of the kiosk mode icon you will see another drop down arrow to set the dashboard refresh rate
* To the left of that is an icon to refresh the dashboard
* To the left of that next to a clock icon is a drop down menu to set the time range for the graphs
  * Initially the time range is set to Last 6 hours


* Moving down and to the left you will see Crawls and Clusters in blue with a drop down menu next to each word
  * Within these drop downs you can choose which crawls and clusters to display


* Beneath Crawls and Clusters are the main dashboard visuals hidden by drop down menus
  * Aggregate will show some aggregate information about all crawls in the database
  * Each Cluster will show average CPU, memory, bandwidth, and storage utilization and can be identified by the cluster number
  * Each Crawl will show visuals specific to that crawl and can be identified by the crawl number


* Any time there is a new crawl or cluster the dashboard must be refreshed
  * Use the dashboard refresh icon in the top right corner to refresh the dashboard