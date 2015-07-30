diag <- read.csv("Patient_Diagnosis.csv")
treat <- read.csv("Patient_Treatment.csv")

first_treat <- subset(treat, !duplicated(treat$Patient_ID))  

names(first_treat)[names(first_treat) == "Treatment_Date"] <- "First_Treatment_Date"

patients <- merge(diag, first_treat, by = "Patient_ID", all = TRUE)

patients$Diagnosis_Date <- as.Date(patients$Diagnosis_Date)
patients$First_Treatment_Date <- as.Date(patients$First_Treatment_Date)

patients$Duration <- patients$First_Treatment_Date - patients$Diagnosis_Date

dur <- subset(patients$Duration, !is.na(patients$Duration))

durpos <- subset(dur, dur > 0)

print("Mean time difference from Diagnosis to First Treatment: ") 
mean(dur)

print("Mean time difference ignoring patients that started Treatment before Diagnosis: ")
mean(durpos)

print("Number patients that started treatment before diagnosis: ")
length(dur) - length(durpos)

