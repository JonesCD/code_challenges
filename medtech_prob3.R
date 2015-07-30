diag <- read.csv("Patient_Diagnosis.csv")
treat <- read.csv("Patient_Treatment.csv")

treat$Treatment_Date <- as.Date(treat$Treatment_Date)

first_treat <- subset(treat, !duplicated(treat$Patient_ID))  

names(first_treat)[names(first_treat) == "Treatment_Date"] <- "First_Treatment_Date"

last_treat <- subset(treat, !duplicated(treat$Patient_ID, fromLast = TRUE))

names(last_treat)[names(last_treat) == "Treatment_Date"] <- "Last_Treatment_Date"

first_treat$Last_Treatment_Date <- last_treat$Last_Treatment_Date

treat_time_all <- first_treat
treat_time_all$Last_Treatment_Date <- last_treat$Last_Treatment_Date
treat_time_all$Treatment_Duration <- treat_time_all$Last_Treatment_Date - treat_time_all$First_Treatment_Date

drugone <- subset(treat_time_all, treat_time_all$Drug_Code == 201)
# drugone
print("Mean treatment duration for drug coded 201 is: ")
mean(drugone$Treatment_Duration)

drugtwo <- subset(treat_time_all, treat_time_all$Drug_Code == 202)
print("Mean treatment duration for drug coded 202 is: ")
mean(drugtwo$Treatment_Duration)

