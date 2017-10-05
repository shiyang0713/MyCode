package hw4;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Procedure2 {

	public static void main(String[] args) {

		try (Connection conn = DriverManager.getConnection("jdbc:sqlserver://localhost:1433;databaseName=DB01", "sa",
				"P@ssw0rd");
				PreparedStatement pstmt = conn.prepareStatement("insert into playlist values(?,?,?)");
				CallableStatement cst = conn.prepareCall("{call gen_seats(?,?,?)}");) {
			// a小題
			conn.setAutoCommit(false);
			pstmt.setString(1, "2016-12-25 13:00");
			pstmt.setInt(2, 1);
			pstmt.setString(3, "A廳");
			pstmt.executeUpdate();
			conn.commit();

			// b小題
			conn.setAutoCommit(false);
			cst.setString(1, "2016-12-29 13:00");
			cst.setInt(2, 1);
			cst.setString(3, "A廳");
			cst.executeUpdate();
			conn.commit();
			conn.close();
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

}
