
report_config = [
    {
        "ReportType": "CricketMatchSummary",
#"Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","L-Win #","L-Win %","","Marks","Darts","MPR","","High Turn","9M","Hat Trick (M)","","Report Link","Event Link"

        "IdentifierColumns": ["Date", "Day", "Legs", "MPR", "9M"],
        "TableName": "cricket_match_summary"
    },
    {
        "ReportType": "01MatchSummary",
#"Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","L-Win #","L-Win %","","Points","Darts","PPR","","Hi Turn","180s","Hi DO","Hi DI",,"Report Link","Event Link"

        "IdentifierColumns": ["Date", "Day", "Legs", "PPR", "180s"],
        "TableName": "x01_match_summary"
    },
    {
        "ReportType": "CricketMatchCounts",
#"Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","5M+","6M+","Trips (M)","Bulls","Dbulls (M)","","Avg 5M+/Leg","Avg 6M+/Leg","Avg Trips/Leg (M)","Avg Bulls/Leg","Avg DBulls/Leg (M)","","5M+/No TB","6+ Marks/ No TB","Trips/No TB (M)","Bulls/ No TB","DBulls/No TB (M)","","Report Link","Event"

        "IdentifierColumns": ["Date", "Day", "Legs", "Bulls"],
        "TableName": "cricket_match_counts"
    },
    {
        "ReportType": "01MatchCounts",
#"Report","League ID","DC Membership","M/F","Date","Day","Division","Season","Away/Guest @ Home/Host","Team","Email","Last Name, FI","Blank","DC","First Name","Legs","100+ Points","100+ Count","180's","","100+ Pts/Leg","100+ Ct/Leg","Avg DO","","100+ Pts No TB","100+ cts No TB","Avg DO No TB","180's No TB","","95+ Points","95+ Count","","Report Link","Event Link"
        "IdentifierColumns": [ "Date", "Day", "100+ Points"],
        "TableName": "x01_match_counts"
    },
    {
        "ReportType": "CricketSeasonSummary",
#"Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","L-Win #","L-Win %","","Points","Darts","MPR","","High Turn","9M","Hat Tricks (M)"
        "IdentifierColumns": ["Matches", "Legs", "MPR", "9M"],
        "TableName": "cricket_season_summary"
    },
    {
        "ReportType": "01SeasonSummary",
#"Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","L-Win #","L-Win %","","Points","Darts","PPR","","Hi Turn","180s","Hi DO","Hi DI","Best Leg"
        "IdentifierColumns": ["Matches", "Legs", "PPR", "180s"],
        "TableName": "x01_season_summary"
    },
    {
        "ReportType": "CricketSeasonCounts",
#"Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","5M+","6M+","Trips (M)","Bulls","DBulls (M)","","Avg 5M+/Leg","Avg 6M+/Leg","Avg Trips/Leg (M)","Avg Bulls/Leg","Avg DBulls/Leg (M)","","5M+/No TB","6+ Marks/ No TB","Trips/No TB (M)","Bulls/ No TB","DBulls/No TB (M)"

        "IdentifierColumns": ["Matches", "Legs", "Bulls"],
        "TableName": "cricket_season_counts"
    },
    {
        "ReportType": "01SeasonCounts",
#"Report","League ID","DC Membership","M/F","Team","Division","Season","Email","Last Name, FI","Blank","DC","First Name","Matches","Legs","100+ Points","100+ Count","180s","","100+ Pts/Leg","100+ Ct/Leg","Avg DO","","100+ Pts No TB","100+ Pts No TB","Avg DO No TB","","180s/Match","180s /Match No TB","","95+ Points","95+ Count"
        "IdentifierColumns": ["Matches", "Legs", "100+ Points"],
        "TableName": "x01_season_counts"
    },
    {
        "ReportType": "MembershipAndEmail",
#"League ID","Division","Match Count","Player Email","Player Name","Team/Division","Host Names","Start Date","Last Date"
        "IdentifierColumns": ["Player Email", "Player Name", "Host Names"],
        "TableName": "membership_and_email"
    },
    {
        "ReportType": "HostDeviceInformation",
#"League ID","Division","Host Name","Host Email","Member Level","Player Email","Player Name","Start Date","Last Date"
        "IdentifierColumns": ["Host Email", "Member Level", "Host Name"],
        "TableName": "host_device_information"
    }
]

column_mapping = {
    "": { "ColumnName": "unknown", "DataType": "VARCHAR(64)" },
    "100+ Count": { "ColumnName": "gte_100_count", "DataType": "INTEGER" },
    "100+ Ct/Leg": { "ColumnName": "gte_100_count_per_leg", "DataType": "DECIMAL(5,2)" },
    "100+ Points": { "ColumnName": "gte_100_points", "DataType": "INTEGER" },
    "100+ Pts No TB": { "ColumnName": "gte_100_points_no_tb", "DataType": "INTEGER" },
    "100+ Pts/Leg": { "ColumnName": "gte_100_pts_per_leg", "DataType": "DECIMAL(5,2)" },
    "100+ cts No TB": { "ColumnName": "gte_100_count_no_tb", "DataType": "INTEGER" },
    "180's No TB": { "ColumnName": "180_count_no_tb", "DataType": "INTEGER" },
    "180's": { "ColumnName": "180_count", "DataType": "INTEGER" },
    "180s /Match No TB": { "ColumnName": "180s /Match No TB", "DataType": "VARCHAR(64)" },
    "180s": { "ColumnName": "180s", "DataType": "VARCHAR(64)" },
    "180s/Match": { "ColumnName": "180s/Match", "DataType": "VARCHAR(64)" },
    "5M+": { "ColumnName": "5M+", "DataType": "VARCHAR(64)" },
    "5M+/No TB": { "ColumnName": "5M+/No TB", "DataType": "VARCHAR(64)" },
    "6+ Marks/ No TB": { "ColumnName": "6+ Marks/ No TB", "DataType": "VARCHAR(64)" },
    "6M+": { "ColumnName": "6M+", "DataType": "VARCHAR(64)" },
    "95+ Count": { "ColumnName": "95+ Count", "DataType": "VARCHAR(64)" },
    "95+ Points": { "ColumnName": "95+ Points", "DataType": "VARCHAR(64)" },
    "9M": { "ColumnName": "9M", "DataType": "VARCHAR(64)" },
    "Avg 5M+/Leg": { "ColumnName": "Avg 5M+/Leg", "DataType": "VARCHAR(64)" },
    "Avg 6M+/Leg": { "ColumnName": "Avg 6M+/Leg", "DataType": "VARCHAR(64)" },
    "Avg Bulls/Leg": { "ColumnName": "Avg Bulls/Leg", "DataType": "VARCHAR(64)" },
    "Avg DBulls/Leg (M)": { "ColumnName": "Avg DBulls/Leg (M)", "DataType": "VARCHAR(64)" },
    "Avg DO No TB": { "ColumnName": "Avg DO No TB", "DataType": "VARCHAR(64)" },
    "Avg DO": { "ColumnName": "Avg DO", "DataType": "VARCHAR(64)" },
    "Avg Trips/Leg (M)": { "ColumnName": "Avg Trips/Leg (M)", "DataType": "VARCHAR(64)" },
    "Away/Guest @ Home/Host": { "ColumnName": "Away/Guest @ Home/Host", "DataType": "VARCHAR(64)" },
    "Best Leg": { "ColumnName": "Best Leg", "DataType": "VARCHAR(64)" },
    "Blank": { "ColumnName": "Blank", "DataType": "VARCHAR(64)" },
    "Bulls": { "ColumnName": "Bulls", "DataType": "VARCHAR(64)" },
    "Bulls/ No TB": { "ColumnName": "Bulls/ No TB", "DataType": "VARCHAR(64)" },
    "DBulls (M)": { "ColumnName": "DBulls (M)", "DataType": "VARCHAR(64)" },
    "DBulls/No TB (M)": { "ColumnName": "DBulls/No TB (M)", "DataType": "VARCHAR(64)" },
    "DC Membership": { "ColumnName": "DC Membership", "DataType": "VARCHAR(64)" },
    "DC": { "ColumnName": "DC", "DataType": "VARCHAR(64)" },
    "Darts": { "ColumnName": "Darts", "DataType": "VARCHAR(64)" },
    "Date": { "ColumnName": "Date", "DataType": "VARCHAR(64)" },
    "Day": { "ColumnName": "Day", "DataType": "VARCHAR(64)" },
    "Dbulls (M)": { "ColumnName": "Dbulls (M)", "DataType": "VARCHAR(64)" },
    "Division": { "ColumnName": "Division", "DataType": "VARCHAR(64)" },
    "Email": { "ColumnName": "Email", "DataType": "VARCHAR(64)" },
    "Event Link": { "ColumnName": "Event Link", "DataType": "VARCHAR(64)" },
    "Event": { "ColumnName": "Event", "DataType": "VARCHAR(64)" },
    "First Name": { "ColumnName": "First Name", "DataType": "VARCHAR(64)" },
    "Hat Trick (M)": { "ColumnName": "Hat Trick (M)", "DataType": "VARCHAR(64)" },
    "Hat Tricks (M)": { "ColumnName": "Hat Tricks (M)", "DataType": "VARCHAR(64)" },
    "Hi DI": { "ColumnName": "Hi DI", "DataType": "VARCHAR(64)" },
    "Hi DO": { "ColumnName": "Hi DO", "DataType": "VARCHAR(64)" },
    "Hi Turn": { "ColumnName": "Hi Turn", "DataType": "VARCHAR(64)" },
    "High Turn": { "ColumnName": "High Turn", "DataType": "VARCHAR(64)" },
    "Host Email": { "ColumnName": "Host Email", "DataType": "VARCHAR(64)" },
    "Host Name": { "ColumnName": "Host Name", "DataType": "VARCHAR(64)" },
    "Host Names": { "ColumnName": "Host Names", "DataType": "VARCHAR(64)" },
    "L-Win #": { "ColumnName": "L-Win #", "DataType": "VARCHAR(64)" },
    "L-Win %": { "ColumnName": "L-Win %", "DataType": "VARCHAR(64)" },
    "Last Date": { "ColumnName": "Last Date", "DataType": "VARCHAR(64)" },
    "Last Name, FI": { "ColumnName": "Last Name, FI", "DataType": "VARCHAR(64)" },
    "League ID": { "ColumnName": "League ID", "DataType": "VARCHAR(64)" },
    "Legs": { "ColumnName": "Legs", "DataType": "VARCHAR(64)" },
    "M/F": { "ColumnName": "M/F", "DataType": "VARCHAR(64)" },
    "MPR": { "ColumnName": "MPR", "DataType": "VARCHAR(64)" },
    "Marks": { "ColumnName": "Marks", "DataType": "VARCHAR(64)" },
    "Match Count": { "ColumnName": "Match Count", "DataType": "VARCHAR(64)" },
    "Matches": { "ColumnName": "Matches", "DataType": "VARCHAR(64)" },
    "Member Level": { "ColumnName": "Member Level", "DataType": "VARCHAR(64)" },
    "PPR": { "ColumnName": "PPR", "DataType": "VARCHAR(64)" },
    "Player Email": { "ColumnName": "Player Email", "DataType": "VARCHAR(64)" },
    "Player Name": { "ColumnName": "Player Name", "DataType": "VARCHAR(64)" },
    "Points": { "ColumnName": "Points", "DataType": "VARCHAR(64)" },
    "Report Link": { "ColumnName": "Report Link", "DataType": "VARCHAR(64)" },
    "Report": { "ColumnName": "Report", "DataType": "VARCHAR(64)" },
    "Season": { "ColumnName": "Season", "DataType": "VARCHAR(64)" },
    "Start Date": { "ColumnName": "Start Date", "DataType": "VARCHAR(64)" },
    "Team": { "ColumnName": "Team", "DataType": "VARCHAR(64)" },
    "Team/Division": { "ColumnName": "Team/Division", "DataType": "VARCHAR(64)" },
    "Trips (M)": { "ColumnName": "Trips (M)", "DataType": "VARCHAR(64)" },
    "Trips/No TB (M)": { "ColumnName": "Trips/No TB (M)", "DataType": "VARCHAR(64)" }
}
