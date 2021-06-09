<br>
<div>
<h1>Examples</h1>
<h3><b>For single profile:</b></h3>
<br>
<code>$ python3 script.py --linkedin_url https://www.linkedin.com/in/charlesashworth</code>

<br>
Output: <br>
<code>
{
    "name": "Charles Ashworth",
        "bio": "Charles Ashworth is the Chief People Officer at Zendrive (www.zendrive.com). Ashworth was also the CHRO at Copper CRM and the CEO of Ashworth Advantage Consulting, an executive coaching firm serving notable customers like Riverbed Technology and LeadGenius. Mr. Ashworth was a key leader at FinancialForce as their Chief People Officer. Mr. Ashworth's career also spans positions as Global Sr. Director of Human Resources at NetSuite Inc. and Hitachi Data Systems. Ashworth spent over 9 years at PeopleSoft during its hyper growth stages in various strategic roles in HCM product working with customers, as well as within the Human Resources and L&D organizations. His talents have been instrumental at notable companies like Riverbed, FinancialForce, NetSuite, PeopleSoft (acquired by Oracle), eBay, and Viator (acquired by TripAdvisor). He also sits on the Governing Board of Directors at NCHRA.",
        "profession": "Chief People Officer | Emerging Tech | Authentic Leadership | Work Culture Enthusiast | Performance Coach",
        "experience": {
            "company": "Zendrive",
            "experience_profession": "Global People and Culture Leader",
            "tenure": "Jan 2020 - Present"
        },
        "education": {
            "institute": "Concordia University Irvine",
            "course": "Bachelors of Science",
            "course_tenure": "Aug 1984 - May 1988"
        }
    }
</code>
<br>
The above code scrapes linkedin profile with username <b>charlesashworth</b>
<hr>
<h3><b>For multiple profiles:</b></h3><br>
<code>linkedin_profiles.csv</code> contains all linkedin profiles that we need to scrap seperated by newline.
<br>
Contents of
<code>linkedin_profiles.csv</code>:
<code>
<br>
https://www.linkedin.com/in/michaeljcase
<br>
https://www.linkedin.com/in/kun-du-3456a0150 <br>
https://www.linkedin.com/in/duane-singh-72966165 <br>
https://www.linkedin.com/in/colepcannon <br>
https://www.linkedin.com/in/duane-singh <br>
</code>
<br>
<br>
<code> $ python3 script.py --filename linkedin_profiles.csv
</code>
<br>
<br>
Output:
<code>
{
  "https://www.linkedin.com/in/michaeljcase\n": {
    "name": "Michael J. Case",
    "bio": "Father to three daughters. Executive Coach. Builder of People & Talent teams for startups. Advisor with PeopleTech Partners. Investor.\n\nFormerly VP of Recruiting and E-team member at Instacart, Recruiting Director at Uber and Salesforce, and Exec Search for Apple, Michael brings 20 years of experience in the HR and Talent space and has built and managed teams of 50+ people. He is an executive coach, advising CEOs and scaling teams for startups in growth mode funded by top VCs in Silicon Valley and beyond: Khosla, a16z, KPCB, Battery, Sequoia, Accel, Lightspeed, Redpoint, Wing, DFJ, and more. \n\nMichael speaks Chinese and Japanese, and lived in Asia for 16 years; he remains active with the startup community in Asia and splits time between San Francisco and Tokyo.\n\nHe also loves to host BBQ parties at home.",
    "profession": "Executive Coach, Talent Consulting, & Executive Search at Neptune People",
    "experience": {
      "company": "Spring Health",
      "experience_profession": "VP Talent (Interim)",
      "tenure": "Dec 2020 - Present"
    },
    "education": {
      "institute": "The University of Chicago - Booth School of Business",
      "course": "MBA",
      "course_tenure": "2008 - 2010"
    }
  },
  "https://www.linkedin.com/in/kun-du-3456a0150\n": {
    "name": "Kun Du",
    "bio": "Computer software engineering graduate student with practical experiences and strong skills in software program development with Java and PHP. Rich experience of web development. Solid knowledge in data structure and algorithm design. Familiar with relational database design.",
    "profession": "Software Engineer at Akamai Technologies",
    "experience": {
      "company": "Akamai Technologies",
      "experience_profession": "Software Engineer II",
      "tenure": "Apr 2020 - Present"
    },
    "education": {
      "institute": "Northeastern University",
      "course": "Master's degree",
      "course_tenure": "2017 - 2019"
    }
  },
  "https://www.linkedin.com/in/duane-singh-72966165\n": {
    "name": "Duane Singh",
    "bio": "Passionate about helping people, personal and professional development, building relationships and pride myself on my work ethic.  \n\nA proud member of the Findem family where we are changing the way companies find their talent.  \n\nDuane Singh\n415-250-8965\nduane@findem.ai",
    "profession": "Account Executive at Findem",
    "experience": {
      "company": "Findem",
      "experience_profession": "Account Executive",
      "tenure": "Mar 2021 - Present"
    },
    "education": {
      "institute": "San Francisco State University",
      "course": "Bachelor's degree",
      "course_tenure": "2001 - Dec 2005"
    }
  },
  "https://www.linkedin.com/in/colepcannon\n": {
    "name": "Cole P Cannon",
    "bio": "Saas Customer Success Leader with 13+ years growing fast-paced and dynamic companies. Responsible for designing, building and executing cross-functional customer success programs in smb and enterprise segments worldwide at both pre and post IPO companies. \n\n\u2022 CSM leadership from private to public company and from $26M to $260M ARR\n\u2022 Promoted 4 times in 5 years from IC to Global Director and led a team of 5 managers and 25 staff globally \n\u2022 Reduced Churn to record lows and increased Upsells to record highs\n\u2022 Excels at hiring, managing and developing staff into rockstar high-performers",
    "profession": "Head of Customer Success at Findem",
    "experience": {
      "company": "Findem",
      "experience_profession": "Head of Customer Success",
      "tenure": "Mar 2021 - Present"
    },
    "education": {
      "institute": "University of San Francisco",
      "course": "Master of Science (MS)",
      "course_tenure": "2010 - 2013"
    }
  },
  "https://www.linkedin.com/in/duane-singh": {
    "name": "Duane Singh",
    "bio": "Passionate about helping people, personal and professional development, building relationships and pride myself on my work ethic.  \n\nA proud member of the Findem family where we are changing the way companies find their talent.  \n\nDuane Singh\n415-250-8965\nduane@findem.ai",
    "profession": "Account Executive at Findem",
    "experience": {
      "company": "Findem",
      "experience_profession": "Account Executive",
      "tenure": "Mar 2021 - Present"
    },
    "education": {
      "institute": "San Francisco State University",
      "course": "Bachelor's degree",
      "course_tenure": "2001 - Dec 2005"
    }
  }
}
</code>
</div>

<br>
