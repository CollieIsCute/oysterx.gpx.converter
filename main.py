#!/usr/bin/env python3
from cmath import sqrt
import sqlite3
import gpxpy

def get_coordinates_from_oysterx_data(oysterx : sqlite3.Connection) -> list :
	cur = oysterx.cursor()
	cur = cur.execute("SELECT latitude, longitude FROM OXStory")
	data = cur.fetchall()
	return data

def get_distance(pA, pB) -> float:
	distance = abs(sqrt(abs(pA[0]-pB[0])**2 + abs(pA[1]-pB[1])**2))
	return distance

def get_gpx_data(data: list) -> str:
	gpx_tree = gpxpy.gpx.GPX()
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx_tree.tracks.append(gpx_track)
	i = 0
	gpx_segment = None
	while i < len(data):
		if i == 0 or get_distance(data[i-1], data[i]) > 0.0005:
			gpx_segment = gpxpy.gpx.GPXTrackSegment()
			gpx_track.segments.append(gpx_segment)
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(data[i][0], data[i][1]))
		i += 1
	return gpx_tree.to_xml()

oysterx = sqlite3.connect("OXDB_user")
coordinateList = get_coordinates_from_oysterx_data(oysterx)

gpx_file = open('oysterX_backup.gpx', 'w')
gpx_file.write(get_gpx_data(coordinateList))
gpx_file.close()