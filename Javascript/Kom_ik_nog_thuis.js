kilometersNaarTankstation = 80;
kilometersPerLiter = 10;
resterendeLiters = 8;
function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
    if (kilometersPerLiter * resterendeLiters >= kilometersNaarTankstation) {
        return true;
    }
    
    return false;
    
}
//test 1
console.log(kanBereikenTankstation(80, 10, 8));
//test 2
console.log(kanBereikenTankstation(80, 10, 7));
//test 3
console.log(kanBereikenTankstation(80, 10, 9));
//test 4
console.log(kanBereikenTankstation(80, 10, 10));
//test 5
console.log(kanBereikenTankstation(80, 10, 11));
//test 6
console.log(kanBereikenTankstation(80, 10, 12));