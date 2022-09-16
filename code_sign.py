from pbxproj import XcodeProject
import sys

# open the project
project = XcodeProject.load('ios/Runner.xcodeproj/project.pbxproj')

team_id = sys.argv[1] # first argument for team_id
issuer_id = sys.argv[2] # second argument for issuer_id
profile_name = 'github_actions'

# Add code sign
project.add_code_sign('iPhone Distribution',
						  team_id,
						  issuer_id,
						  profile_name)

# save the project, otherwise your changes won't be picked up by Xcode
project.save()