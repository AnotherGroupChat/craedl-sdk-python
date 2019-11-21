import craedl
profile = craedl.auth()
profile.get_project("Testing").get_data().get("experiments").create_directory("results")
profile.get_project("Testing").get_data().get("experiments").create_file("outputs")
# profile.get_project("Testing").get_data().get("experiments").create_file("/home/dylan/src/pdpdpd/src/configs/data/copper.pbtxt")
