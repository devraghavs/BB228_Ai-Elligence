def generate_trains(src,dest,journey_date,train_type,night_shift):
    ls = [
            {
                "src_to_inter_stop":
                    {
                        "waiting_time": "",
                        "id" : 0,
                        "train_no": "1",
                        "train_type": "A",
                        "src": "JP",
                        "dest": "AG",
                        "dep_time_at_src": "10:00",
                        "arr_time_at_dest": "12:00",
                        "journey_time": "500",
                        "Route_score": 12
                    },
                "inter_stop_to_dest":
                    {
                        "train_no": "2",
                        "train_type": "B",
                        "src": "AG",
                        "dest": "JU",
                        "dep_time_at_src": "14:00",
                        "arr_time_at_dest": "20:00",
                        "journey_time": "300",
                        "Route_score": 0
                    }
            },
            {
                "src_to_inter_stop":
                    {
                        "waiting_time": "",
                        "id" : 0,
                        "train_no": "1",
                        "train_type": "A",
                        "src": "JP",
                        "dest": "AG",
                        "dep_time_at_src": "10:00",
                        "arr_time_at_dest": "12:00",
                        "journey_time": "500",
                        "Route_score": 12
                    },
                "inter_stop_to_dest":
                    {
                        "train_no": "2",
                        "train_type": "B",
                        "src": "AG",
                        "dest": "JU",
                        "dep_time_at_src": "14:00",
                        "arr_time_at_dest": "20:00",
                        "journey_time": "300",
                        "Route_score": 0
                    }
            }
        ]
    return ls