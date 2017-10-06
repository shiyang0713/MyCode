create proc loop99 @vi int, @vj int
as
declare @i int =1,@j int =1,@str varchar(150);
   
	while (@i<=@vi)
	  begin
		set @str=''
		while (@j<=@vj)
		  begin 
		   
			set @str=@str+format(@j,'00') + '*' + format(@i,'00') + '=' + format(@i*@j,'00') + CHAR(10) 
			set @j=@j+1
		  end;
	  set @i=@i+1
	  set @j=1
	  print @str
	end;


go

