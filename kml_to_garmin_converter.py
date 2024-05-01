import xml.etree.ElementTree as ET
import csv

def kml_to_csv(kml_file, csv_file):
    with open(kml_file, 'r', encoding='utf-8') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as out_f:
            csv_writer = csv.writer(out_f)
            csv_writer.writerow(['WaypointName', 'Latitude', 'Longitude', 'Description'])
            
            for placemark in root.findall('.//{http://www.opengis.net/kml/2.2}Placemark'):
                name = placemark.find('.//{http://www.opengis.net/kml/2.2}name').text
                description = placemark.find('.//{http://www.opengis.net/kml/2.2}description').text
                coordinates = placemark.find('.//{http://www.opengis.net/kml/2.2}coordinates').text.split(',')
                latitude = coordinates[1]
                longitude = coordinates[0]
                
                csv_writer.writerow([name, latitude, longitude, description])

# File Name:
kml_file = 'VFR WP 320.kml'
csv_file = 'garmin_waypoints.csv'
kml_to_csv(kml_file, csv_file)

#Created By Yarin Twina