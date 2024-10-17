program TestParserDelphi;

{$APPTYPE CONSOLE}

var
  a, b, c: Integer;

begin
  a := 15;
  b := 25;
  c := a + b;

  if c > 30 then
    Writeln('The sum is greater than 30')
  else
    Writeln('The sum is not greater than 30');

  for a := c downto 0 do
    Writeln('Current value of a: ', a);

  Writeln('Program finished.');
end.
