cursor.execute("""
        #     SELECT value,id ,property_code
        #     FROM measurements
        #     ORDER BY value ASC
        #     LIMIT 1
        # """)