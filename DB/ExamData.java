package EvergreenClient;

public class ExamData {
    int studentID;
    int examID;
    int examStartTime;
    int examDuration;
    int examEndTime;
    String status;

    public ExamData(int studentID, int examID, int examStartTime, int examDuration, String status) {
        this.studentID = studentID;
        this.examID = examID;
        this.examStartTime = examStartTime;
        this.examDuration = examDuration;
        this.status = status;
        this.examEndTime = examStartTime + examDuration;
    }

    public int getStudentID() {
        return studentID;
    }

    public void setStudentID(int studentID) {
        this.studentID = studentID;
    }

    public int getExamID() {
        return examID;
    }

    public void setExamID(int examID) {
        this.examID = examID;
    }

    public int getExamStartTime() {
        return examStartTime;
    }

    public void setExamStartTime(int examStartTime) {
        this.examStartTime = examStartTime;
    }

    public int getExamDuration() {
        return examDuration;
    }

    public void setExamDuration(int examDuration) {
        this.examDuration = examDuration;
    }

    public int getExamEndTime() {
        return examEndTime;
    }

    public void setExamEndTime(int examEndTime) {
        this.examEndTime = examEndTime;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "ExamData{" +
                "studentID=" + studentID +
                '}';
    }
}