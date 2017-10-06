--delete  from seats
--select * from seats
--select * from m_room

begin
  declare   @v_row     int;
  declare   @v_col     int;
  declare   @v_ptime   varchar(20); 
  declare   @v_movie   int;
  declare   @v_roomid  varchar(10);
  declare   @x_row     int;
  declare   @x_col     int;

  --�]�w�ܼƭ�
  set @v_ptime  = '2016-12-25 13:00';
  set @v_movie  = 1;
  set @v_roomid = 'A�U';

  --���d�M ���w�U�|���y��� row, col
  select @v_row = seat_row , @v_col = seat_col
  from   m_room
  where  roomid = @v_roomid;

  --�ھڮy��� @v_row, @v_col ���ͮy���
  set @x_row = 1;       
    while ( @x_row  <= @v_row )
      begin
        set @x_col = 1;     
        while ( @x_col  <= @v_col )
          begin
          insert into seats values ( @v_ptime, @v_movie, format(@x_row ,'00')+ '-' + format(@x_col,'00'), '0', NULL);
          set  @x_col = @x_col +1  
          end; 
		set @x_row = @x_row +1
		set  @x_col = 1  
      end;
end;