#queries used in app.py
queries = {"login": """
                SELECT FirstName, LastName, Email, Password, RoleID 
                FROM users 
                WHERE (Email = %s OR Phone = %s);

            """,
        "signup": """INSERT INTO users (FirstName, LastName, Email, Phone, Password, RoleID)
                    VALUES (%s, %s, %s, %s, %s, %s)""",

        'equipment_info': "SELECT * FROM equipment",

        "lab_test_request":"""
                INSERT INTO requests (UserID, LabID, RequestDate, Details, EquipmentID, Status, StartTime, EndTime, SampleID)
                VALUES (%s, '1', NOW(), %s, %s, %s, %s, %s, %s);

            """,

        "latest_request" :  """
                SELECT r.RequestID, r.RequestDate, r.Details, r.Status, r.StartTime, r.EndTime, 
                       u.FirstName, u.LastName, l.LabName, e.EquipmentName, s.SampleName
                FROM requests r
                JOIN users u ON r.UserID = u.UserID
                LEFT JOIN labs l ON r.LabID = l.LabID
                LEFT JOIN equipment e ON r.EquipmentID = e.EquipmentID
                LEFT JOIN samples s ON r.SampleID = s.SampleID
                WHERE u.Email = %s
                ORDER BY r.RequestDate DESC 
                LIMIT 1
            """,
        "request_display":  """ 
                SELECT 
            r.RequestID, 
            u.Email AS UserEmail, 
            e.EquipmentName AS Equipment, 
            s.SampleName AS Sample, 
            r.RequestDate AS RequestDate, 
            r.StartTime AS StartTime, 
            r.EndTime AS EndTime
        FROM 
            requests r
        JOIN 
            users u ON r.UserID = u.UserID
        LEFT JOIN 
            equipment e ON r.EquipmentID = e.EquipmentID
        LEFT JOIN 
            samples s ON r.SampleID = s.SampleID
        ORDER BY 
            r.RequestDate DESC; 
            """,
        "update_accept_request": """
                UPDATE requests
                SET Status = 'accepted', manager_id = %s
                WHERE RequestID = %s
            """,
        "update_reject_request":"""
                UPDATE requests 
                SET Status = 'rejected'
                WHERE RequestID = %s
            """
}

