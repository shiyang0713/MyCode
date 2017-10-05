create procedure gen_seats( @v_ptime  varchar(20),@v_movie  int,@v_roomid varchar(10) )
as
BEGIN
  DECLARE   @v_row     int;
  DECLARE   @v_col     int;
  DECLARE   @x_row     int;
  DECLARE   @x_col     int;

  --�]�w�ܼƭ�
  
  --���d�M ���w�U�|���y��� row, col
  select @v_row = seat_row , @v_col = seat_col
  from   m_room
  where  roomid = @v_roomid

  --�ھڮy��� @v_row, @v_col ���ͮy���
  SET @x_row = 1;       
    WHILE ( @x_row  <= @v_row )
      BEGIN
        SET @x_col = 1;     
        WHILE ( @x_col  <= @v_col )
          BEGIN
            insert into seats values ( @v_ptime, @v_movie, format(@x_row,'00')+'-'+format(@x_col,'00'), '0', NULL);
               set @x_col=@x_col+1
          END; 
         set @x_row=@x_row+1
      END;
END;


