/* ISSCityLookup.java */

import com.maxmind.geoip.*;
import java.io.IOException;

/* Use the GeoIP Java API with GeoIP City database for ISS passive recon reports */
/* Usage: java ISSCityLookup 4.2.2.2 */

class ISSCityLookup {
    public static void main(String[] args) {

	if ( args.length < 2 ) {
		System.err.println("Usage: ISSCityLookup <GeoDBPath> <IP> ");
		System.exit(1);
	}else{
		
	
			try {
					LookupService cl = new LookupService(args[0],
							  LookupService.GEOIP_MEMORY_CACHE );
						  Location l2 = cl.getLocation(args[1]);
					System.out.println( args[1] +
													"->" + l2.countryCode +
													"," + l2.countryName +
													"," + l2.region +
													"," + regionName.regionNameByCode(l2.countryCode, l2.region) +
													"," + l2.city +
													"," + l2.postalCode +
													"," + timeZone.timeZoneByCountryAndRegion(l2.countryCode, l2.region));

					cl.close();
			  }
			  catch (IOException e) {
					System.out.println("IO Exception" + e.getMessage() );
			  }
			}
	}
}
