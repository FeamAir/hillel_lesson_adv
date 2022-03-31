/*
Total summary price
and tracks.
*/

SELECT TrackId, SUM(UnitPrice) as TotalPrice, COUNT(TrackId) as TotalTracks
FROM invoice_items
group by TrackId;

