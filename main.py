query = '''SELECT
    phrase,
    groupArray((toHour(dt), count())) AS views_by_hour
FROM
    phrases_views
WHERE
    campaign_id = 1111111
    AND toDate(dt) = today()
GROUP BY
    phrase
ORDER BY
    phrase;'''