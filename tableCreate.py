conn = sqlite3.connect('example.db')
c = conn.cursor()

#create table only once
c.execute('''CREATE TABLE exceltable (
[FAMILY COURT WATCH QUESTIONAIRE] TEXT,
[Volunteer] TEXT,
[Case Short Title] TEXT,
[Case Number] TEXT,
[Hearing Date] TEXT,
[Hearing Time] TEXT,
[Department] TEXT,
[Judge/Commissioner] TEXT,
[     Male] TEXT,
[     Female] TEXT,
[Petitioner's Name] TEXT,
[     Male] TEXT,
[     Female] TEXT,
[Respondent's Name] TEXT,
[     Male] TEXT,
[     Female] TEXT,
[Ex Parte Hearing] TEXT,
[Law and Motion Hearing] TEXT,
[Hearing] TEXT,
[Trial] TEXT,
[Settlement Conference] TEXT,
[Other  (mediation agreement)] TEXT,
[COURTROOM APPEARANCES] TEXT,
[Petitioner: Represented] TEXT, 
[Petitioner: Pro se] TEXT,
[Respondent: Represented] TEXT, 
[Respondent: Pro se] TEXT,
[Attorney for Child(ren) Name:] TEXT,
[    Male] TEXT,
[    Female] TEXT,
[Other:] TEXT,
[If one of the parties was not present, what reason was given for non-appearance?] TEXT,
[Appeared by phone: Yes] TEXT,
[Appeared by phone: No] TEXT,
[Appeared by Skype: Yes] TEXT,
[Appeared by Skype: No] TEXT,
[Minute Order provided at end: Yes] TEXT,
[Minute Order provided at end: No] TEXT,
[ISSUES/LITIGATION] TEXT,
[     Divorce] TEXT,
[     Child Custody] TEXT,
[     Child Support] TEXT,
[     Child Visitation] TEXT,
[     Restraining Order] TEXT,
[     Spousal Support] TEXT,
[     Contempt] TEXT,
[     Attorney Fees] TEXT,
[     Other: ] TEXT,
[Was the case continued to a future date: Yes] TEXT,
[     Date of continued hearing:] TEXT,
[Was the case continued to a future date: No] TEXT,
[Were any stipulations presented: Yes] TEXT,
[      Did judge ask if parties understood: Yes] TEXT, 
[      Did judge ask if parties understood: No] TEXT,
[Were any stipulations presented: No] TEXT,
[CHILD CUSTODY/VISIT/ SUPPORT ORDERS] TEXT,
[Custody/visit orders in place prior to hearing:] TEXT,  
[      Joint physical custody] TEXT,
[      Joint legal custody] TEXT,
[      Legal custody: Petitioner] TEXT,
[      Legal custody: Respondent] TEXT,
[      Physical custody: Petitioner] TEXT,
[      Physical custody: Respondent] TEXT,
[      Unsupervised visitation to: Petitioner] TEXT,
[      Unsupervised visitation to: Repondent] TEXT,
[      Supervised visitation to: Petitioner] TEXT,
[      Supervised visitation to: Repondent] TEXT,
[Request to change custody: Yes] TEXT,
[      Made by Petitioner] TEXT,
[      Made by Respondent] TEXT,
[Request to change custody: No] TEXT,
[Request to change visitation: Yes] TEXT,
[      Made by Petitioner] TEXT,
[      Made by Respondent] TEXT,
[Request to change visitation: No] TEXT,
[Reason for request to change custody/visitation] TEXT,
[           Domestic violence] TEXT,  
[           Child abuse/neglect] TEXT,
[           Relocation] TEXT,
[           Educational issues] TEXT,
[           Child behavioral issues] TEXT,
[           Child's wishes] TEXT,
[           Developmental stage of child] TEXT,
[           Other:] TEXT, 
[Changes made to custody order: Yes] TEXT,
[           Sole legal to Petitioner] TEXT,
[           Sole legal to Respondent] TEXT,
[           Joint legal to Petitioner] TEXT,
[           Joint legal to Respondent] TEXT,
[           Sole physical to Petitioner] TEXT,
[           Sole physical to Respondent] TEXT,
[           Joint physical/primary to Petitioner] TEXT, 
[           Joint physical/primary to Respondent] TEXT,
[Changes made to visitation order: Yes] TEXT,
[           Increased for Petitioner] TEXT,
[           Increased for Respondent] TEXT,
[           Terminated for Petitioner] TEXT,
[           Terminated for Respondent] TEXT, 
[           Supervised for Petitioner] TEXT,
[           Supervised for Respondent] TEXT, 

[Changes to custody or visitation: No] TEXT, 
[Prior or current allegations of DV/CA against a party receiving increased custody/visits: Yes] TEXT, 
[Prior or current allegations of DV/CA against a party receiving increased custody/visits: No] TEXT, 
[Prior or current allegations of DV/CA against a party receiving increased custody/visits: UNK] TEXT, 
[Party requesting increase behind support: Yes] TEXT, 
[Party requesting increase behind support: No] TEXT, 
[Party requesting increase behind support: UNK] TEXT, 
[Was a party requesting change in support: Yes] TEXT, 
[	Primary custodial parent] TEXT,
[   Other parent] TEXT,
[   Support increased] TEXT,
[   Support decreased] TEXT,
[   No change in support] TEXT,
[Was a party requesting change in support: No] TEXT,
[Was a party requesting change in support: UNK] TEXT,
[DUE PROCESS/CONSTITUTIONAL RIGHTS] TEXT,
[Did a court reporter make a record: Yes] TEXT,
[Did a court reporter make a record: No] TEXT,
[	Did a party/minor attny request/object: Yes] TEXT,
[		Did hearing proceed anyway: Yes] TEXT,
[       Did hearing proceed anyway: No] TEXT,
[	Did a party/minor attny request/object: No] TEXT,
[   Did a party ask to audio/videotape: Yes] TEXT,
[       Was the request granted: Yes] TEXT,
[       Was the request granted: No] TEXT,
[	Did a party ask to audio/videotape: No] TEXT,
[Did meeting occur in chambers: Yes] TEXT,
[	Who went into chambers] TEXT,
[    	Petitioner's attorney] TEXT,
[       Respondent's attorney] TEXT,
[       Child's attorney] TEXT,
[       Petitioner] TEXT,
[       Respondent] TEXT,
[       Court reporter] TEXT,
[If petitioner/respondent excluded, why:] TEXT,
[If record made of in-chambers meeting by court reporter, did judge seal record: Yes] TEXT,
[If record made of in-chambers meeting by court reporter, did judge seal record: No] TEXT,
[Court appointee report/info  presented: Yes] TEXT,
[		Author: Mediator] TEXT,
[		Author:  Evaluator/investigator] TEXT,
[       Author: Court appointed therapist] TEXT,
[       Author: Co-parenting coordinator] TEXT,
[	Did a party object to report/info: Yes] TEXT,
[       Did not receive report 10 days prior] TEXT,
[       Report/info hearsay] TEXT,
[       Report/info  not authenticated] TEXT,
[   Judge ruled on objection: Sustained] TEXT,
[   Judge ruled on objection: Overruled] TEXT,
[       Was objecting party able to examine: Yes] TEXT, 
[       Was objecting party able to examine: No] TEXT, 
[        	Was a hearing date set? Yes] TEXT,
[           Was a hearing date set? No] TEXT,
[  	Did a party object to report/info: No] TEXT,
[Court appointee report/info  presented: No] TEXT,
[Did anyone else present information regarding something by someone not present: Yes] TEXT,
[	Who presented the info:] TEXT,
[   Was a hearsay objection made: Yes] TEXT,
[    	By whom:] TEXT,
[       Did court hear/consider anyway: Yes] TEXT,
[       Did court hear/consider anyway: No] TEXT,
[ 	Was a hearsay objection made: No] TEXT,
[Did anyone else present information regarding something by someone not present: No] TEXT,
[Party denied right to evidence/ witness: Yes] TEXT,
[	Petitioner] TEXT,
[ 	Respondent] TEXT,
[ 	Reason for denial:] TEXT,
[ 	Future date to present evidence: Yes] TEXT,
[ 	Future date to present evidence: No] TEXT,
[Party denied right toevidence/ witness: No] TEXT,
[Party prevented from discovery: Yes] TEXT,
[	Reason:] TEXT,
[Party prevented from discovery: No] TEXT,
[Parties give equal opportunity to speak: Yes] TEXT,
[Parties give equal opportunity to speak: No] TEXT,
[	Petitioner given less opportunity] TEXT,
[	Respondent given less opportunity] TEXT,
[Party discouraged from speaking publicly: Yes] TEXT,
[	What was judge's comment:] TEXT,
[Party discouraged from speaking publicly: No] TEXT,
[JUDICIAL CONDUCT/DEMEANOR] TEXT,
[Was audience asked to identify self: Yes] TEXT,
[Was audience asked to identify self: No] TEXT,
[Was anybody (not witness) excluded: Yes] TEXT,
[	What reason given:] TEXT,
[Was anybody (not witness) excluded: No] TEXT,
[Was judge courteous/respectful: Yes] TEXT,
[Was judge courteous/respectful: No] TEXT,
[	To whom was judge disrespectful:] TEXT,
[ 	Describe:] TEXT,
[  	How did disrespected person react:] TEXT,
[Did anyone else speak disrespectfully: Yes] TEXT,
[	Who was disrespectful:] TEXT,
[  	Who was disrespected:] TEXT,
[  	Describe:] TEXT,
[  	How did disrespected person react:] TEXT,
[  	How did judge handle situation:] TEXT,
[Did anyone else speak disrespectfully: No] TEXT,
[Did anyone raise vioce/act aggressive: Yes] TEXT,
[	Who was aggressive:] TEXT,
[  	Who was aggressed against:] TEXT,



####Ted’s stuff####
[      Describe:] TEXT, 
[      How did aggressed against person react:] TEXT, 
[      How did judge handle situation:] TEXT, 
[Did anyone raise voice/act aggressive: No] TEXT, 
[Did a party cry: Yes] TEXT, 
[     Who cried:] TEXT, 
[     How did judge respond] TEXT, 
[Did a party cry: No] TEXT, 
[Did judge appear irritated/angry at pro se: Yes] TEXT, 
[      How did judge behave/what was said:] TEXT, 
[Did judge appear irritated/angry at pro se: No] TEXT, 
[Did judge appear irritated/angry at pro se: N/A] TEXT, 
[Did a party seem incapable: Yes] TEXT, 
[      Describe condition of party:] TEXT, 
[      How did judge handle situation:] TEXT, 
[Did a party seem incapable: No] TEXT, 
[IMPRESSIONS] TEXT, 
[Did it seem to be even playing field: Yes] TEXT, 
[Did it seem to be even playing field: No] TEXT, 
[      Who was disadvantaged:] TEXT, 
[      Why:] TEXT, 
[Did pro se seem disadvantaged by attny: Yes] TEXT, 
[Did pro se seem disadvantaged by attny: No] TEXT, 
[Did pro se seem disadvantaged by attny: N/A] TEXT, 
[Were both held to same standard: Yes] TEXT, 
[Were both held to same standard: No] TEXT, 
[    Impression why not held to same standard: ] TEXT, 
[Familiarity between anyone/bias: Yes] TEXT, 
[     Describe:] TEXT, 
[Familiarity between anyone/bias: No] TEXT, 
[Favoritism/antagonism by judge: Yes] TEXT, 
[     Describe:] TEXT, 
[Favoritism/antagonism by judge: No] TEXT, 
[Other Remarks:] TEXT, 
[ACCOMODATIONS] TEXT, 
[Was an interpreter present? Yes] TEXT, 
[    Interpreter for Petitioner] TEXT, 
[    Interpreter for Respondent] TEXT, 
[Was an interpreter present? No] TEXT, 
[Did either party ask for accommodation: Yes] TEXT, 
[     Requested by Petitioner] TEXT,
[     Requested by Respondent] TEXT,
[     What accommodations were requested?] TEXT,
[     What accommodations were provided?] TEXT,
[     Did the judge reveal a diagnosis: Yes] TEXT,
[     Did the judge reveal a diagnosis:  No] TEXT,
[Did either party ask for accommodation: No] TEXT,
[Did either party ask for accommodation: UNK] TEXT,
[DOMESTIC VIOLENCE (CV)] TEXT,
[Protective order in place: Yes] TEXT,
[     Petitioner protected] TEXT,
[     Respondent protected] TEXT,
[     Child(ren) protected] TEXT,
[Protective order in place: No] TEXT,
[Protective order in place: UNK] TEXT,
[Restrained party want to terminate: Yes] TEXT,
[     Was protective order dismissed: Yes] TEXT,
[     Was protective order dismissed: No] TEXT,
[Restrained party want to terminate: No] TEXT,
[Did anyone raise DV allegations: Yes] TEXT,
[     Petitioner raised allegations] TEXT,
[     Respondent raised allegations] TEXT,
[     Other raised allegations: ] TEXT,
[         Physical] TEXT,
[         Sexual] TEXT,
[         Verbal/psychological] TEXT,
[         Stalking] TEXT,
[         Other] TEXT,
[      Did alleger ask for restraining order: Yes] TEXT,
[          Was request granted: Yes] TEXT,
[                Judge explained conditions: Yes] TEXT,
[                Judge explained conditions: No] TEXT,
[                Judge order weapons turned in: Yes] TEXT,
[                Judge order weapons turned in: No] TEXT,
[                Other safety orders:] TEXT,
[          Was request granted: No] TEXT,
[                 Reason for denial:] TEXT,
[         Party with protection to have contact: Yes] TEXT,
[                  Mediation   ] TEXT,
[                  Co-parenting classes] TEXT,
[                  Child exchanges] TEXT,
[                         Where exchanges to take place:] TEXT,
[                  Other] TEXT,
[         Party with protection to have contact: No] TEXT,
[         Was protected party accused: Yes] TEXT,
[         Was protected party accused: No] TEXT,
[         Were allegations minimized: Yes] TEXT,
[               What gesture/comment:] TEXT,
[         Were allegations minimized: No] TEXT,
[         Provision to leave safely: Yes] TEXT,
[         Provision to leave safely: No] TEXT,
[Did anyone raise DV allegations: No] TEXT,
[CHILD ABUSE] TEXT,
[Did anyone raise allegations of child abuse: Yes] TEXT,
[     Petitioner raised allegations] TEXT,
[     Respondent raised allegations] TEXT,
[     Other raised allegations:] TEXT,
[         Physical] TEXT,
[         Sexual] TEXT,
[         Verbal/psychological] TEXT,


####Phillip’s stuff####
[         Other] TEXT,
[     Age 0-4] TEXT,
[     Age 5-10] TEXT,
[     Age 11-14] TEXT,
[     Age over 14] TEXT,
[     Was allegation already reported to LE: Yes ] TEXT,
[     Was allegation already reported to LE: No ] TEXT,
[     Was allegation already reported to LE: UNK] TEXT,
[      Was investigative report ordered: Yes] TEXT,
[           MDIT/law enforcement] TEXT,
[           Child Protective Services] TEXT,
[            Probation Dept] TEXT,
[            FC evaluator: Name] TEXT,
[            FC mediator: Name] TEXT,
[            Other:] TEXT,
[             If sex abuse alleged, FC 3118 ordered: Yes] TEXT,
[                   Name of eval/investigator:] TEXT,
[             If sex abuse alleged, FC 3118 ordered: No] TEXT,
[      Was investigative report ordered: No] TEXT,
[Was child ordered to contact with abuser: Yes] TEXT,
[       Unsupervised contact] TEXT,
[       Contact supervised by professional] TEXT,
[       Contact supervised by non-pro neutral] TEXT,
[       Contact supervised by family/friend] TEXT,
[       Parent child therapy] TEXT,
[       Other:] TEXT,
[Was child ordered to contact with abuser: No] TEXT,
[Did alleger ask for protection for child: Yes] TEXT,
[      Was request granted: Yes] TEXT,
[      Was request granted: No] TEXT,
[          Reason for denial:] TEXT,
[Was alleger accused: Yes] TEXT,
[      Who accused alleger:] TEXT,
[Was alleger accused: No] TEXT,
[Did judge minimize: Yes] TEXT,
[     Describe gestures/comments] TEXT,
[Did judge minimize: No] TEXT,
[Did anyone raise allegations of child abuse: No] TEXT,
[CHILD'S INPUT] TEXT,
[Request child appear: Yes] TEXT,
[     Petitioner request] TEXT,
[     Respondent request] TEXT,
[     Child's attorney] TEXT,
[     Other: ] TEXT,
[     Judge agreed] TEXT,
[     Judge denied] TEXT,
[          Reason for denial:] TEXT,
[     Judge reserved for future hearing] TEXT,
[          Date of hearing] TEXT,
[Attorney for child: Yes] TEXT,
[      Child's attorney] TEXT,
[      Guardian Ad Litem] TEXT,
[       Best Interest Attorney] TEXT,
[Where physically in courtroom:] TEXT,
[Appear to be aligned/prejudiced: Yes] TEXT,
[      How show favoritism:] TEXT,
[Appear to be aligned/prejudiced: No] TEXT,
[Did child's attorney give report/input: Yes] TEXT,
[     Was child present to testify: Yes] TEXT,
[           Under 10 testified] TEXT,
[           Age 10-14 testified] TEXT,
[           Over 14 testified] TEXT,
[      Examined on witness stand] TEXT,
[            Objection to open court question: Yes] TEXT,
[                  Who objected:] TEXT,
[            Objection to open court question: No] TEXT,
[            Was child placed under oath: Yes] TEXT,
[            Was child placed under oath: No] TEXT,
[            Judge questioned child] TEXT,
[            Child's attorney questioned child] TEXT,
[            Petitioner's attorney questioned child] TEXT,
[            Petitioner questioned child] TEXT,
[            Respondent's attorney questioned child] TEXT,
[            Respondent questioned child] TEXT,
[            Party denied ability to question: Yes] TEXT,
[                   Petitioner denied] TEXT,
[                   Respondent denied] TEXT,
[           Party denied ability to question: No] TEXT,
[           How did child react to examination:] TEXT,
[    Questioned  in chambers] TEXT,
[          Did a party object: Yes] TEXT,
[          Did a party object: No] TEXT,
[          Petitioner went to chambers] TEXT,
[          Petitioner's attorney went to chambers] TEXT,
[          Respondent went to chambers] TEXT,
[          Respondent's attorney went to chambers] TEXT,
[          Child's attorney went to chambers] TEXT,
[          Court reporter went to chambers] TEXT,
[              Court prevent access to record: Yes] TEXT,
[              Court prevent access to record: No] TEXT,
[    Questioned  by remote access] TEXT,
[          At courthouse, video separate location ] TEXT,
[          Away from courthouse by Skype] TEXT,
[         Other:] TEXT,
[         Child under oath: Yes] TEXT,
[         Child under oath: No] TEXT,
[         Judge questioned child] TEXT,
[         Child's attorney questioned child] TEXT,
[         Petitioner questioned child] TEXT,
[         Petitioner's attorney questioned child] TEXT,
[         Respondent questioned child] TEXT,
[         Respondent's attorney questioned child] TEXT,
[         Other questioned child] TEXT,
[          Was a party denied question child: Yes] TEXT,
[                 Petitioner prevented questions] TEXT,
[                 Respondent prevented questions] TEXT,
[          Was a party denied question child: No] TEXT,
[     Was child present to testify: No] TEXT,
[Request child appear: No] TEXT
)''')

for row in exceldata:
    c.execute('INSERT INTO exceltable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
conn.commit()