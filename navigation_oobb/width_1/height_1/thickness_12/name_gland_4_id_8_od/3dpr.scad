$fn = 50;


difference() {
	union() {
		translate(v = [30, 0, 0]) {
			rotate(a = [180, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -7.5000000000]) {
							cylinder(h = 15, r = 3.7500000000);
						}
						translate(v = [0, 0, 2.1250000000]) {
							cylinder(h = 5.3750000000, r = 6.0000000000);
						}
						translate(v = [-7.0000000000, -4.5000000000, -7.5000000000]) {
							cube(size = [7.0000000000, 9, 5.3750000000]);
						}
					}
					union() {
						translate(v = [0, 0, -7.5000000000]) {
							cylinder(h = 15, r = 2.1250000000);
						}
					}
				}
			}
		}
		translate(v = [0, 0, -7.5000000000]) {
			cylinder(h = 15, r = 3.7500000000);
		}
		translate(v = [0, 0, 2.1250000000]) {
			cylinder(h = 5.3750000000, r = 6.0000000000);
		}
		translate(v = [-7.0000000000, -4.5000000000, -7.5000000000]) {
			cube(size = [7.0000000000, 9, 5.3750000000]);
		}
	}
	union() {
		translate(v = [0, 0, -7.5000000000]) {
			cylinder(h = 15, r = 2.1250000000);
		}
		translate(v = [-250.0000000000, 0, -250.0000000000]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, 0, -250.0000000000]) {
			cube(size = [500, 500, 500]);
		}
		translate(v = [-250.0000000000, 0, -250.0000000000]) {
			cube(size = [500, 500, 500]);
		}
	}
}