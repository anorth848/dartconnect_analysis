
report_config = [
    {
        "ReportType": "CricketMatchSummary",
# "Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","L-Win #","L-Win %","","Marks","Darts","MPR","","High Turn","9M","Hat Trick (M)","","Report Link","Event Link"

        "IdentifierColumns": ["Date", "Day", "Legs", "MPR", "9M"]
    },
    {
        "ReportType": "01MatchSummary",
# "Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","L-Win #","L-Win %","","Points","Darts","PPR","","Hi Turn","180s","Hi DO","Hi DI",,"Report Link","Event Link"

        "IdentifierColumns": ["Date", "Day", "Legs", "PPR", "180s"]
    },
    {
        "ReportType": "CricketMatchCounts",
# "Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","5M+","6M+","Trips (M)","Bulls","Dbulls (M)","","Avg 5M+/Leg","Avg 6M+/Leg","Avg Trips/Leg (M)","Avg Bulls/Leg","Avg DBulls/Leg (M)","","5M+/No TB","6+ Marks/ No TB","Trips/No TB (M)","Bulls/ No TB","DBulls/No TB (M)","","Report Link","Event"

        "IdentifierColumns": ["Date", "Day", "Legs", "Bulls"]
    },
    {
        "ReportType": "01MatchCounts",
        #"Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","100+ Points","100+ Count","180's","","100+ Pts/Leg","100+ Ct/Leg","Avg DO","","100+ Pts No TB","100+ cts No TB","Avg DO No TB","180's No TB","","95+ Points","95+ Count","","Report Link","Event Link"
        "IdentifierColumns": [ "Date", "Day", "100+ Points"]
    },
    {
        "ReportType": "CricketSeasonSummary",
        # "Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","L-Win #","L-Win %","","Points","Darts","MPR","","High Turn","9M","Hat Tricks (M)"
        "IdentifierColumns": ["Matches", "Legs", "MPR", "9M"]
    },
    {
        "ReportType": "01SeasonSummary",
# "Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","L-Win #","L-Win %","","Points","Darts","PPR","","Hi Turn","180s","Hi DO","Hi DI","Best Leg"
        "IdentifierColumns": ["Matches", "Legs", "PPR", "180s"]
    },
    {
        "ReportType": "CricketSeasonCounts",
# "Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","5M+","6M+","Trips (M)","Bulls","DBulls (M)","","Avg 5M+/Leg","Avg 6M+/Leg","Avg Trips/Leg (M)","Avg Bulls/Leg","Avg DBulls/Leg (M)","","5M+/No TB","6+ Marks/ No TB","Trips/No TB (M)","Bulls/ No TB","DBulls/No TB (M)"

        "IdentifierColumns": ["Matches", "Legs", "Bulls"]
    },
    {
        "ReportType": "01SeasonCounts",
#"Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","100+ Points","100+ Count","180s","","100+ Pts/Leg","100+ Ct/Leg","Avg DO","","100+ Pts No TB","100+ Pts No TB","Avg DO No TB","","180s/Match","180s /Match No TB","","95+ Points","95+ Count"
        "IdentifierColumns": ["Matches", "Legs", "100+ Points"]
    },
    {
        "ReportType": "MembershipAndEmail",
# "League ID","Division","Match Count","Player Email","Player Name","Team/Division","Host Names","Start Date","Last Date"
        "IdentifierColumns": ["Player Email", "Player Name", "Host Names"]

    },
    {
        "ReportType": "HostDeviceInformation",
# "League ID","Division","Host Name","Host Email","Member Level","Player Email","Player Name","Start Date","Last Date"
        "IdentifierColumns": ["Host Email", "Member Level", "Host Name"]
    }
]
