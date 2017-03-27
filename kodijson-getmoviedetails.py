# Get all the properties of the movie
JSON_req = {"jsonrpc": "2.0",
                    "method": "VideoLibrary.GetMovieDetails",
                    "params": {"movieid": 51,
                    "properties": ["art",
                                        "cast",
                                        "dateadded", "director",
                                        "fanart", "file",
                                        "genre",
                                        "imdbnumber",
                                        "lastplayed",
                                        "mpaa",
                                        "originaltitle",
                                        "playcount", "plot", "plotoutline", "premiered",
                                        "rating", "runtime",
                                        "setid", "sorttitle", "streamdetails", "studio",
                                        "tagline", "thumbnail", "title", "trailer",
                                        "userrating",
                                        "votes",
                                        "writer"]},
                      "id": "1"}
log('JSON_req string = %s' % json.dumps(JSON_req))
JSON_result = utils.executeJSON(JSON_req)
log('JSON VideoLibrary.GetMovieDetails result = %s' % JSON_result)
