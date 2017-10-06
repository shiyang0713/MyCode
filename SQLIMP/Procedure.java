import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Timestamp;
import java.util.Calendar;

class process {
	public void insertPlayList(String date,int movie,String room_ID){

		try (Connection connection = DriverManager.getConnection("jdbc:sqlserver://localhost:1433;databaseName=db01",
				"sa", "P@ssw0rd");
				PreparedStatement pstat = connection.prepareStatement("insert into playlist values (?,?,?)")) {
			connection.setAutoCommit(false);
			
			
			pstat.setString(1, date);
			pstat.setInt(2, movie);
			pstat.setString(3, room_ID);
			pstat.execute();

			System.out.println("Playlist insertion has been finished.");
			connection.commit();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		
	}
	
	public void listAllSeat(int movie){
		try (Connection connection = DriverManager.getConnection("jdbc:sqlserver://localhost:1433;databaseName=db01",
				"sa", "P@ssw0rd");
				PreparedStatement selectCommand=connection.prepareStatement("select * from m_room where roomid='AÆU'");
				PreparedStatement pstat = connection.prepareStatement("insert into seats values (?,?,?,?,?)")) {
			connection.setAutoCommit(false);
			ResultSet rs= selectCommand.executeQuery();
			rs.next();
			int row=rs.getInt("seat_row");
			int col=rs.getInt("seat_col");			
			
			Calendar cal=Calendar.getInstance();
			Timestamp date=new Timestamp(cal.getTimeInMillis());
			String year=date.toString().substring(0, 16);
			pstat.setString(1,year );
			pstat.setInt(2, movie);
			pstat.setString(4, "1");
			pstat.setInt(5, 0);
			
			System.out.println(String.format("%-20s%-8s%-6s","ptime","movie","SeatNumber"));
			int count=0;
			for(int i=1;i<=row;i++){
				for(int j=1;j<=col;j++){
					String SeatNumber=String.format("%02d-%02d", i, j);
					pstat.setString(3, SeatNumber);
					pstat.addBatch();
					System.out.println(String.format("%-20s%-8s%-6s",year,movie,SeatNumber));
					count++;
					if(count%50==0){
						pstat.executeBatch();					
					}
				}
			}
			pstat.executeBatch();
			connection.commit();
			System.out.println(count+" data has been inserted.");
			
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}
	
}

public class Procedure {

	public static void main(String[] args) {
			
		process test=new process();
		test.insertPlayList("2017-06-19 11:45", 1, "AÆU");
		
		test.listAllSeat(1);
		

		
	}

}
