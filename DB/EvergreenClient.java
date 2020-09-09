package EvergreenClient;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.Duration;
import java.util.*;

public class EvergreenClient {
    private static String centerName = "Evergreen";
    private  String centerID = "1";
    private int numOfRooms = 2;      //number of test rooms in this center
    private int numOfStations = 4;   //number of stations in each room

    public EvergreenClient(String centerID) {
        this.centerID = centerID;
    }
    public static void main(String[] args) {
        EvergreenClient EC = new EvergreenClient("1");
        List<ExamData> data = EC.request(EC.getTestDate());
        EC.scheduleTest(data);
    }

    String getTestDate() {
        String date = "";
        System.out.println("Please enter a test date (format mm-dd-yyyy): ");
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        try {
            date = reader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (date.length() == 0) {
            System.out.println("A test date has to be provided!");
            getTestDate();
        } else if (date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-') {
            System.out.println("The date format is wrong, it has to be mm-dd-yyyy");
            getTestDate();
        }
        return date;
    }
    List<ExamData> request(String date){
        String query = "http://127.0.0.1:8000/tests/test_list?test_center=1&date=" + date;
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(query))
                .timeout(Duration.ofMinutes(1))
                .build();
        HttpResponse response = null;
        try {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return parse(response.body().toString());
    }
    static List<ExamData> parse (String responseBody) {
        List<ExamData> students = new ArrayList<ExamData>();
        JSONArray originalData = new JSONArray(responseBody);
        for (int i = 0; i < originalData.length(); i++) {
            JSONObject temp = originalData.getJSONObject(i);
            ExamData student = new ExamData(temp.getInt("studentID"), temp.getInt("examID"),
                    temp.getInt("examStartTime"), temp.getInt("examDuration"), temp.getString("status") );
            students.add(student);
        }
        return students;
    }
    void scheduleTest(List<ExamData> students) {
        //convert examStartTime, examDuration from string to int;
        int examStartTime = 0;  //8.5 means 8:30 AM; 15.5 means 15:30
        int examDuration = 0;
        LinkedList<ExamData>[][] stations = new LinkedList[numOfRooms][numOfStations];    //matrix of stations

        //step 1: sort testData based on examStartTime
        Collections.sort(students, new sortByTime());
        //step 2: arrange exam stations sequentially
        for (int i = 0; i < students.size(); i++) {
            boolean scheduled = false;
            for (int room = 0; room < numOfStations; room++) {
                for (int seat = 0; seat < numOfStations; seat++) {
                    if (stations[room][seat].size() == 0 || stations[room][seat].peekLast().examEndTime < students.get(i).examStartTime) {
                        stations[room][seat].add(students.get(i));
                        scheduled = true;
                    }
                }
            }
            if (!scheduled) {
                System.out.println("Warning: fail to schedule this test! Student ID: " + students.get(i).studentID);
            }
        }
        //step 3: display results
        for (int room = 0; room < numOfStations; room++) {
            for (int seat = 0; seat < numOfStations; seat++) {
                System.out.println("Room " + room + ", Station " + seat + ":");
                System.out.println(stations[room][seat].toString());
            }
        }
    }

    class sortByTime implements Comparator<ExamData> {
        public int compare(ExamData a, ExamData b) {
            return a.examStartTime - b.examStartTime;
        }
    }

    public static String getCenterName() {
        return centerName;
    }

    public static void setCenterName(String centerName) {
        EvergreenClient.centerName = centerName;
    }

    public String getCenterID() {
        return centerID;
    }

    public void setCenterID(String centerID) {
        this.centerID = centerID;
    }

    public int getNumOfRooms() {
        return numOfRooms;
    }

    public void setNumOfRooms(int numOfRooms) {
        this.numOfRooms = numOfRooms;
    }

    public int getNumOfStations() {
        return numOfStations;
    }

    public void setNumOfStations(int numOfStations) {
        this.numOfStations = numOfStations;
    }

}

