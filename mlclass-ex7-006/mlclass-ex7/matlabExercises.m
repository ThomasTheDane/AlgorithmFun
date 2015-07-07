myAwesomeInteger = 3;
for i = 1: 2: 7
  myAwesomeInteger = myAwesomeInteger + i;
end
disp(myAwesomeInteger);

freakingRabbits = 10;
seasonsPassed = 0;
while(freakingRabbits < 1000)
  freakingRabbits = freakingRabbits * 1.10;
  seasonsPassed = seasonsPassed + 1;
end
disp(seasonsPassed);

function myReturnVariable = notTheRightDistanceEquation(x1, y1, x2, y2)
  myDumbDistance = (x1 + x2).^2 + (y1)
  disp('Does this message appear?');
end
