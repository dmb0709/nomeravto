program RegionCodeLookup;

uses
  SysUtils, Crt;

type
  TRegionDict = TStringList;

var
  RegionDict: TRegionDict;

procedure LoadRegionData(const FileName: string);
var
  F: TextFile;
  Line: string;
  Key, Value: string;
  SeparatorPos: Integer;
begin
  RegionDict := TStringList.Create;
  AssignFile(F, FileName);
  try
    Reset(F);
    while not Eof(F) do
    begin
      ReadLn(F, Line);
      SeparatorPos := Pos(':', Line);
      if SeparatorPos > 0 then
      begin
        Key := Copy(Line, 1, SeparatorPos - 1);
        Value := Copy(Line, SeparatorPos + 1, Length(Line));
        RegionDict.Values[Key] := Value;
      end;
    end;
  finally
    CloseFile(F);
  end;
end;

procedure HandleSignal(Sig: LongInt); cdecl;
begin
  WriteLn(' Выход по Ctrl+C!');
  Halt(0);
end;

procedure MainLoop;
var
  Code: string;
begin
  while True do
  begin
    WriteLn('Введите код региона! 0 - для выхода');
    ReadLn(Code);
    if Code = '0' then
      Halt(0);
    if RegionDict.IndexOfName(Code) = -1 then
    begin
      TextColor(Red);
      WriteLn('Такого кода в базе нет!');
      TextColor(LightGray);
    end
    else
    begin
      TextColor(Green);
      WriteLn(RegionDict.Values[Code]);
      TextColor(LightGray);
    end;
  end;
end;

begin
  // Очистка экрана
  ClrScr;

  // Загрузка данных из файла
  LoadRegionData('short.db');

  // Обработка сигнала Ctrl+C
  Signal(SIGINT, @HandleSignal);

  // Основной цикл программы
  MainLoop;
end.
