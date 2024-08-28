
default_groups = [
    'Teachers', 
    'Support Staff (all non-instructional)', 
    'Building and District Administrators',
    'Parents'
]

default_survey = {
    'description': 'After identifying your participant group on the next screen, please rank this leader on a scale of 1-5 '+
        'for each quality described. While we strongly encourage you to share your perspective in all areas, a "no response" '+
        'option is provided for those who may not feel comfortable responding to a given item. ',
    'welcome': 'Thank you for taking a few minutes to provide this leader with candid feedback regarding his/her job performance. '+
        'Your responses will remain confidential and will be shared only as part of group information to help this leader learn '+
        'more about perceptions of his/her work and in establishing performance goals. Your email address is requested for the sole '+
        'purpose of survey management and will not be shared in any reports retained by the district. Please enter your email address, '+
        'the passcode provided and click \'validate\' when you are ready to proceed. ',
    'closing': 'You have completed the survey. Thank you again for your valued input which will be used to improve our organization. If'+
        ' you have additional insights or wish to provide feedback on the survey itself you are encouraged to contact your human resources office.  ',
    'closed_system': 'Survey is offered to a minimum of seven predetermined participants for each group. Each will be forward a discreet'+
        ' password for access. Dimensions: As stated, please use definitions of dimensions included in the report to better define the standard dimensions. ',
    'group': 'To which group do you belong?'
}

default_dimensions = [
    {
        'name': 'Knowledge/Core Competency',
        'description': 'intended to measure the leader’s perceived knowledge, background and preparation for the assignment.',
        'color': '#D63A71',
        'icon': '/media//icons/default_icons/icon-knowledge.png'
    },
    {
        'name': 'Relationships',
        'description': 'Intended to measure the leader’s perceived ability to listen empathetically, communicate and relate with all constituents.',
        'color': '#ECA09C',
        'icon': '/media//icons/default_icons/icon-relationships.png'
    },
    {
        'name': 'Vision',
        'description': 'To assess the leader’s strengths in setting a clear, inspiring and realistic direction for the school district.',
        'color': '#E0B81F',
        'icon': '/media//icons/default_icons/icon-vision.png'
    },
    {
        'name': 'Management',
        'description': 'Assessing the leader’s abilities and attention to basic operational details of the school district.',
        'color': '#AEAEB0',
        'icon': '/media//icons/default_icons/icon-management.png'
    },
    {
        'name': 'Ethics/Standards',
        'description': 'Intended to assess the leader’s perceived tendency to base decisions and actions on high ethical standards and principles.',
        'color': '#C49A6B ',
        'icon': '/media//icons/default_icons/icon-ethics.png'
    },
    {
        'name': 'Advocacy',
        'description': 'Measures leaders efforts and inclination to advocate for the district to external audiences.',
        'color': '#AFCE5C',
        'icon': '/media//icons/default_icons/icon-advocacy.png'
    },
    {
        'name': 'Developer',
        'description': 'Measuring the leaders inclination and efforts to develop and grow the strengths of others.',
        'color': '#DE6045',
        'icon': '/media//icons/default_icons/icon-developer.png'
    },
    {
        'name': 'Leadership Style',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Open Text',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Hogan HDS',
        'description': 'Exploration of Hogan Derailers ',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Knowledge/Core Competency (MPS)',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Developer (MPS)',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Relator (MPS)',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Climate (MPS) ',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Standards (MPS)',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
    {
        'name': 'Text Response (MPS)',
        'description': '',
        'color': '#8fc1ef',
        'icon': '/media//icons/default_icons/icon-default.png'
    },
]

default_questions = [
    {
        #Knowledge/Core Competency
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': 'Is personally involved in teaching and learning.',
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': 'Shares new approaches related to the improvement of teaching and learning.',
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': 'Shows a firm grasp of our district’s data.',
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': 'Uses data to drive improvement.',
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': 'Is knowledgeable about the key issues and challenges related to his/her department.',
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Knowledge/Core Competency',
        'type': 'radio',
        'text': "Shows a firm grasp of our students' data.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Relationships
    {
        'dimension': 'Relationships',
        'type': 'radio',
        'text': "Is highly approachable.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Relationships',
        'type': 'radio',
        'text': "Demonstrates effective listening skills.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Relationships',
        'type': 'radio',
        'text': "Enjoys social interaction and engagement with others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Relationships',
        'type': 'radio',
        'text': "Builds strong rapport with others in the school community.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Relationships',
        'type': 'radio',
        'text': "Has an open door policy.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #vision
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Has a clear sense about the priorities and best course for our district.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Shares enthusiasm about the future of our district.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Has realistic expectations about what the organization can achieve.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Communicates the district's vision and direction.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Articulates clear targets and measures for district progress.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Develops clear targets for student success.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Effectively communicates district vision.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Vision',
        'type': 'radio',
        'text': "Has a clear sense about the priorities and best course for his/her building or department.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Management
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Works to maintain a pleasant physical environment for student learning.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Demonstrates knowledge about the district’s financial situation and takes steps to ensure the district’s continued financial health. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Has a strong vision related to district technology.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Demonstrates attention to detail.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Encourages collaboration and cooperation.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Management',
        'type': 'radio',
        'text': "Has a strong vision related to the use of technology.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Ethics/Standards
    {
        'dimension': 'Ethics/Standards',
        'type': 'radio',
        'text': "Keeps student growth as the top priority in decisions and actions. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Ethics/Standards',
        'type': 'radio',
        'text': "Considers and discusses ethical aspects of important decisions.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Ethics/Standards',
        'type': 'radio',
        'text': "Models what he/she asks of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Advocacy
    {
        'dimension': 'Advocacy',
        'type': 'radio',
        'text': "Advocates for the district with governmental decision-makers or other external audiences.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Developer
    {
        'dimension': 'Developer',
        'type': 'radio',
        'text': "Works to grow the strengths and skills of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Developer',
        'type': 'radio',
        'text': "Encourages innovation.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Developer',
        'type': 'radio',
        'text': "Welcomes different perspectives and contrary opinions from others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Developer',
        'type': 'radio',
        'text': "Shows preference for a non-authoritarian coaching style.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Developer',
        'type': 'radio',
        'text': "Encourages and supports others in developing new skills.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Leadership style
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Remains calm and composed in the face of difficult problems or challenges.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Appears to trust the abilities and motivations of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Appears self-confident in pursuing new approaches and making changes.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Models strong and effective customer service.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Demonstrates appropriate humility about his/her own abilities, successes and failures.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Connects and communicates well with others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Seems to prefer getting things done to getting all the credit or being in the spotlight.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Ideas appear to be grounded and practical.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Delegates and empowers others to do their jobs.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Supports unpopular positions if he/she believes it is the right thing to do.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Plans thoughtfully and avoids unnecessary risks.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Is receptive to criticism from others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Easily accepts responsibility for failures.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Offers candid feedback to others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Makes decisions in a timely way.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Regularly asks others for feedback.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Follows through on commitments made to others at work.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Generously shares credit for success with staff and others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Carefully considers the impact of all important decisions.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Allows other voices to be heard during meetings and discussions.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Follows through on projects that are started.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Has reasonable and fair expectations about the work of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Has clear positions and others know where he/she stands on important issues.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Leadership Style',
        'type': 'radio',
        'text': "Remains calm and composed in addressing district challenges and initiatives.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Open Text
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Please share any other suggestions or comments that you believe would help this leader. Particularly, provide specific feedback regarding any areas you rated as serious performance concerns. (A text response, at least NA, must be provided in order to continue.) ",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Please share any other comments that you believe would help this leader to be more effective. (A text response, at least NA, must be provided in order to continue.)",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Briefly share any observations you have about this leader's greatest strengths. (A text response, at least NA, must be provided in order to continue.)",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Please share any other suggestions that you believe would help this leader. Particularly, provide specific feedback regarding any areas you rated as serious performance concerns. (A text response, at least NA, must be provided in order to continue.)",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Finally, please share any thoughts you may have regarding this survey process. (A text response, at least NA, must be provided in order to continue.)",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "In a few words, describe any new understanding you have gained about your strengths or performance risks?",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Did the Hogan reports and related discussion help to confirm any prior beliefs you had about your strengths or performance risks? If so, describe in a few words.",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "What are a couple things you would like feedback on as we we develop your confidential 360 assessment?",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Please share any emerging thoughts you have regarding a strength that you will leverage and grow.",
    },
    
    {
        'dimension': 'Open Text',
        'type': 'long_answer',
        'text': "Please share any emerging thoughts you may have regarding an opportunity for improvement an growth.",
    },
    #Hogan HDS
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Remains calm during stressful situations.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Remains resilient in solving difficult problems.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Appears to be steady and self-assured.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Does not dwell on past mistakes.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Appears to trust others’ intentions and motives.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Avoids finding fault with others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is forgiving of others' mistakes.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Seems open and eager when meeting new people.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Appears to be willing and interested in trying new things.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is decisive, assertive and willing to express opinions.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is social engaging and appears to enjoy being around others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is viewed as accessible, warm and cooperative.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is sympathetic and sensitive to others’ feelings.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Follows through on promises made to others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Expresses appreciation for the contributions of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is flexible and open to input from others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is appropriately humble, unassuming and unpretentious.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Seems to be aware of his/her own abilities and limitations.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Seems down to earth and willing to roll up sleeves if necessary to get the job done.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Avoids unnecessary risks and makes few mistakes.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is dependable, reliable, structured and predictable.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Seems genuine, straightforward and trustworthy.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is restrained and reserved when appropriate.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is generally focused and task-oriented.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Usually avoids drama and adheres to social norms.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Ideas are appropriately conventional and understood by others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is open to the ideas and perspectives of others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Ideas usually appear to be grounded and practical.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is relaxed and forgiving when working with others.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Works quickly and is action-oriented.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is flexible and comfortable working in ambiguous situations when required.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is independent and self-sufficient in making decisions.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Is self-reliant and tough-minded.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    {
        'dimension': 'Hogan HDS',
        'type': 'radio',
        'text': "Will challenge the process and other leaders when the situation requires.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    #Knowledge/Core Competency (MPS)
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal uses information about student achievement to promote high achievement for all students. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal is knowledgeable about best practice regarding curriculum and instruction.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal models high quality leadership and decision making strategies. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal ensures the selection of a high performing staff.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal understands and utilizes appropriate communication technology.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The principal uses data to guide positive changes within the building.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor uses information about student achievement to promote high achievement for special education students. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor is knowledgeable about best practice regarding special education.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor models high quality leadership and decision making strategies. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor ensures the selection of a high performing staff.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor understands and utilizes appropriate communication technology. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    },
    
    {
        'dimension': 'Knowledge/Core Competency (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor uses data to guide positive changes within the building.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    #Developer (MPS)
    {
        'dimension': 'Developer (MPS)',
        'type': 'radio',
        'text': "The principal provides leadership in the area of individual teacher support and development.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    
    {
        'dimension': 'Developer (MPS)',
        'type': 'radio',
        'text': "The principal has communicated to me my strengths and areas for growth",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    
    {
        'dimension': 'Developer (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor provides leadership in the area of individual teacher support and development. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    
    {
        'dimension': 'Developer (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor has communicated to me my strengths and areas for growth.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    #Relator (MPS)
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The principal communicates effectively with different audiences.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The principal actively listens and seeks to clarify the intent of others in the school environment.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The principal creates opportunities for parents/guardians to be involved and show support for the school. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The principal is accessible on a regular basis to meet the needs of the staff.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor communicates in a timely and effective manner with different audiences.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor actively listens and seeks to clarify the intent of others in the Special Education Department.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor creates opportunities for parents/guardians to be involved and show support for the Special Education Department. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Relator (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor is accessible on a regular basis to meet the needs of the staff.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    #Climate (MPS)
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The principal creates a climate for leading positive change. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The principal sets the tone for a safe learning environment. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The principal understands the impact of the building culture for school success. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The principal employs conflict-resolution and problem-solving strategies appropriately.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The principal works collaboratively with the school staff to create a positive learning environment.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor creates a climate for leading positive change. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor sets the tone for a safe learning environment. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor understands the impact of the building culture for school success",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor employs conflict-resolution and problem-solving strategies appropriately.  ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Climate (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor works collaboratively with the department staff to create a positive learning environment.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    #Standards (MPS)
    {
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The principal sets high standards that result in high achievement and accountability for all learners. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The principal sets high standards and accountability for all employees. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {   
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The principal exemplifies high standards of professional practice and behavior.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {   
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor sets high standards that result in high achievement and accountability for all learners with special education needs. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {   
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor sets high standards and accountability for special education staff. ",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    {   
        'dimension': 'Standards (MPS)',
        'type': 'radio',
        'text': "The Special Education Supervisor exemplifies high standards of professional practice and behavior.",
        'choices': [
            ('Strongly Disagree', 1),
            ('Disagree', 2),
            ('Neutral', 3),
            ('Agree', 4),
            ('Strongly Agree', 5),
            ('No Response', '')
        ]
    }, 
    #Text Response (MPS)
    {   
        'dimension': 'Standards (MPS)',
        'type': 'long_answer    ',
        'text': "Briefly share any observations you have about this leader's greatest strengths. (A text response, at least NA, must be provided in order to continue.)"
    }, 
    {   
        'dimension': 'Standards (MPS)',
        'type': 'long_answer    ',
        'text': "Please share any other suggestions that you believe would help this leader. Particularly, provide specific feedback regarding any areas you rated as serious performance concerns. (A text response, at least NA, must be provided in order to continue.)"
    },
    {   
        'dimension': 'Standards (MPS)',
        'type': 'long_answer    ',
        'text': "Finally, please share any thoughts you may have regarding this survey process. (A text response, at least NA, must be provided in order to continue.)"
    },

]