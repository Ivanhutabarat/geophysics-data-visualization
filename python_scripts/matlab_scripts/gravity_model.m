data = readtable('datasets/gravity_data.csv');
plot(data.Location, data.Gravity, 'o-');
xlabel('Location');
ylabel('Gravity (m/s²)');
title('Gravity Data Visualization');
