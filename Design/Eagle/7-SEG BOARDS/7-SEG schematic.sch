<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="6.5.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Parts">
<packages>
<package name="LED_DRIVER_ASSEMBLY_CHIP">
<pad name="GNDC" x="-7.62" y="3.81" drill="0.8" shape="square"/>
<pad name="SCLC" x="-5.08" y="3.81" drill="0.8" shape="square"/>
<pad name="DRAIN7C" x="-2.54" y="3.81" drill="0.8" shape="square"/>
<pad name="DRAIN6C" x="0" y="3.81" drill="0.8" shape="square"/>
<pad name="DRAIN5C" x="2.54" y="3.81" drill="0.8" shape="square"/>
<pad name="DRAIN4C" x="5.08" y="3.81" drill="0.8" shape="square"/>
<pad name="A1C" x="7.62" y="3.81" drill="0.8" shape="square"/>
<pad name="A0C" x="10.16" y="3.81" drill="0.8" shape="square"/>
<pad name="GC" x="10.16" y="-16.51" drill="0.8" shape="square"/>
<pad name="A2C" x="7.62" y="-16.51" drill="0.8" shape="square"/>
<pad name="DRAIN3C" x="5.08" y="-16.51" drill="0.8" shape="square"/>
<pad name="DRAIN2C" x="2.54" y="-16.51" drill="0.8" shape="square"/>
<pad name="DRAIN1C" x="0" y="-16.51" drill="0.8" shape="square"/>
<pad name="DRAIN0C" x="-2.54" y="-16.51" drill="0.8" shape="square"/>
<pad name="SDAC" x="-5.08" y="-16.51" drill="0.8" shape="square"/>
<pad name="VCCC" x="-7.62" y="-16.51" drill="0.8" shape="square"/>
<pad name="DRAIN7OUT" x="-5.08" y="7.62" drill="0.8" shape="square"/>
<pad name="DRAIN6OUT" x="-2.54" y="7.62" drill="0.8" shape="square"/>
<pad name="VCCOUT1" x="0" y="7.62" drill="0.8" shape="square"/>
<pad name="DRAIN5OUT" x="2.54" y="7.62" drill="0.8" shape="square"/>
<pad name="DRAIN4OUT" x="5.08" y="7.62" drill="0.8" shape="square"/>
<pad name="DRAIN0OUT" x="-2.54" y="-20.32" drill="0.8" shape="square"/>
<pad name="DRAIN1OUT" x="0" y="-20.32" drill="0.8" shape="square"/>
<pad name="DRAIN2OUT" x="2.54" y="-20.32" drill="0.8" shape="square"/>
<pad name="DRAIN3OUT" x="5.08" y="-20.32" drill="0.8" shape="square"/>
<pad name="12V" x="-12.7" y="-11.43" drill="0.8" shape="square"/>
<pad name="VCC" x="-12.7" y="-8.89" drill="0.8" shape="square"/>
<pad name="SDA" x="-12.7" y="-6.35" drill="0.8" shape="square"/>
<pad name="SCL" x="-12.7" y="-3.81" drill="0.8" shape="square"/>
<pad name="GND" x="-12.7" y="-1.27" drill="0.8" shape="square"/>
<pad name="SEGPIN3" x="2.54" y="-35.56" drill="1" shape="square"/>
<pad name="SEGPIN2" x="7.62" y="-35.56" drill="1" shape="square"/>
<pad name="SEGPIN1" x="12.7" y="-35.56" drill="1" shape="square"/>
<pad name="SEGPIN4" x="-2.54" y="-35.56" drill="1" shape="square"/>
<pad name="SEGPIN5" x="-7.62" y="-35.56" drill="1" shape="square"/>
<pad name="DRAIN0JUMP" x="-2.54" y="-33.02" drill="0.8" shape="square"/>
<pad name="DRAIN1JUMP" x="0" y="-33.02" drill="0.8" shape="square"/>
<pad name="VCCJUMP2" x="2.54" y="-33.02" drill="0.8" shape="square"/>
<pad name="DRAIN2JUMP" x="5.08" y="-33.02" drill="0.8" shape="square"/>
<pad name="DRAIN3JUMP" x="7.62" y="-33.02" drill="0.8" shape="square"/>
<pad name="DRAIN0RES" x="-2.54" y="-30.48" drill="0.8" shape="square"/>
<pad name="DRAIN1RES" x="0" y="-30.48" drill="0.8" shape="square"/>
<pad name="VCCRES2" x="2.54" y="-30.48" drill="0.8" shape="square"/>
<pad name="DRAIN2RES" x="5.08" y="-30.48" drill="0.8" shape="square"/>
<pad name="DRAIN3RES" x="7.62" y="-30.48" drill="0.8" shape="square"/>
<pad name="DRAIN7JUMP" x="-2.54" y="13.97" drill="0.8" shape="square"/>
<pad name="DRAIN6JUMP" x="0" y="13.97" drill="0.8" shape="square"/>
<pad name="VCCJUMP1" x="2.54" y="13.97" drill="0.8" shape="square"/>
<pad name="DRAIN5JUMP" x="5.08" y="13.97" drill="0.8" shape="square"/>
<pad name="DRAIN4JUMP" x="7.62" y="13.97" drill="0.8" shape="square"/>
<pad name="GNDX1" x="12.7" y="12.7" drill="0.8" shape="square"/>
<pad name="VX1" x="15.24" y="12.7" drill="0.8" shape="square"/>
<pad name="GNDX2" x="12.7" y="10.16" drill="0.8" shape="square"/>
<pad name="VX2" x="15.24" y="10.16" drill="0.8" shape="square"/>
<pad name="GNDX3" x="12.7" y="7.62" drill="0.8" shape="square"/>
<pad name="VX3" x="15.24" y="7.62" drill="0.8" shape="square"/>
<pad name="GNDNEXT" x="13.97" y="-1.27" drill="0.8" shape="square"/>
<pad name="SCLNEXT" x="13.97" y="-3.81" drill="0.8" shape="square"/>
<pad name="SDANEXT" x="13.97" y="-6.35" drill="0.8" shape="square"/>
<pad name="VCCNEXT" x="13.97" y="-8.89" drill="0.8" shape="square"/>
<pad name="12VNEXT" x="13.97" y="-11.43" drill="0.8" shape="square"/>
<pad name="A1SET" x="7.62" y="8.255" drill="0.8" shape="square"/>
<pad name="A0SET" x="10.16" y="8.255" drill="0.8" shape="square"/>
<pad name="GSET" x="10.16" y="-20.955" drill="0.8" shape="square"/>
<pad name="A2SET" x="7.62" y="-20.955" drill="0.8" shape="square"/>
<wire x1="-2.54" y1="-16.51" x2="-2.54" y2="-20.32" width="0.8128" layer="16"/>
<wire x1="0" y1="-20.32" x2="0" y2="-16.51" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-16.51" x2="2.54" y2="-20.32" width="0.8128" layer="16"/>
<wire x1="5.08" y1="-20.32" x2="5.08" y2="-16.51" width="0.8128" layer="16"/>
<wire x1="7.62" y1="-16.51" x2="7.62" y2="-20.955" width="0.8128" layer="16"/>
<wire x1="10.16" y1="-20.955" x2="10.16" y2="-16.51" width="0.8128" layer="16"/>
<wire x1="10.16" y1="3.81" x2="10.16" y2="8.255" width="0.8128" layer="16"/>
<wire x1="7.62" y1="8.255" x2="7.62" y2="3.81" width="0.8128" layer="16"/>
<wire x1="5.08" y1="3.81" x2="5.08" y2="7.62" width="0.8128" layer="16"/>
<wire x1="2.54" y1="7.62" x2="2.54" y2="3.81" width="0.8128" layer="16"/>
<wire x1="0" y1="3.81" x2="0" y2="7.62" width="0.8128" layer="16"/>
<wire x1="-2.54" y1="7.62" x2="-2.54" y2="3.81" width="0.8128" layer="16"/>
<wire x1="-5.08" y1="3.81" x2="-5.08" y2="7.62" width="0.8128" layer="16"/>
<wire x1="7.62" y1="-33.02" x2="12.7" y2="-33.02" width="0.8128" layer="16"/>
<wire x1="12.7" y1="-33.02" x2="12.7" y2="-35.56" width="0.8128" layer="16"/>
<wire x1="7.62" y1="-35.56" x2="5.08" y2="-35.56" width="0.8128" layer="16"/>
<wire x1="5.08" y1="-35.56" x2="5.08" y2="-33.02" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-33.02" x2="2.54" y2="-35.56" width="0.8128" layer="16"/>
<wire x1="0" y1="-33.02" x2="0" y2="-35.56" width="0.8128" layer="16"/>
<wire x1="0" y1="-35.56" x2="-2.54" y2="-35.56" width="0.8128" layer="16"/>
<wire x1="-2.54" y1="-33.02" x2="-7.62" y2="-33.02" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="-33.02" x2="-7.62" y2="-35.56" width="0.8128" layer="16"/>
<pad name="P$1" x="-2.54" y="-26.67" drill="0.8" shape="square"/>
<pad name="P$2" x="0" y="-26.67" drill="0.8" shape="square"/>
<pad name="P$3" x="2.54" y="-26.67" drill="0.8" shape="square"/>
<pad name="P$4" x="5.08" y="-26.67" drill="0.8" shape="square"/>
<pad name="P$5" x="7.62" y="-26.67" drill="0.8" shape="square"/>
<wire x1="7.62" y1="-26.67" x2="7.62" y2="-30.48" width="0.8128" layer="16"/>
<wire x1="5.08" y1="-30.48" x2="5.08" y2="-26.67" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-26.67" x2="2.54" y2="-30.48" width="0.8128" layer="16"/>
<wire x1="0" y1="-30.48" x2="0" y2="-26.67" width="0.8128" layer="16"/>
<wire x1="-2.54" y1="-26.67" x2="-2.54" y2="-30.48" width="0.8128" layer="16"/>
<pad name="P$6" x="-2.54" y="16.51" drill="0.8" shape="square"/>
<pad name="P$7" x="0" y="16.51" drill="0.8" shape="square"/>
<pad name="P$8" x="2.54" y="16.51" drill="0.8" shape="square"/>
<pad name="P$9" x="5.08" y="16.51" drill="0.8" shape="square"/>
<pad name="P$10" x="7.62" y="16.51" drill="0.8" shape="square"/>
<wire x1="-2.54" y1="13.97" x2="-2.54" y2="16.51" width="0.8128" layer="16"/>
<wire x1="0" y1="16.51" x2="0" y2="13.97" width="0.8128" layer="16"/>
<wire x1="2.54" y1="13.97" x2="2.54" y2="16.51" width="0.8128" layer="16"/>
<wire x1="5.08" y1="16.51" x2="5.08" y2="13.97" width="0.8128" layer="16"/>
<wire x1="7.62" y1="13.97" x2="7.62" y2="16.51" width="0.8128" layer="16"/>
<wire x1="15.24" y1="12.7" x2="15.24" y2="10.16" width="0.8128" layer="16"/>
<wire x1="15.24" y1="10.16" x2="15.24" y2="7.62" width="0.8128" layer="16"/>
<wire x1="12.7" y1="12.7" x2="12.7" y2="10.16" width="0.8128" layer="16"/>
<wire x1="12.7" y1="7.62" x2="12.7" y2="10.16" width="0.8128" layer="16"/>
<wire x1="-12.7" y1="-1.27" x2="-7.62" y2="-1.27" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="-1.27" x2="-7.62" y2="3.81" width="0.8128" layer="16"/>
<wire x1="-12.7" y1="-8.89" x2="-7.62" y2="-8.89" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="-8.89" x2="-7.62" y2="-16.51" width="0.8128" layer="16"/>
<wire x1="-12.7" y1="-11.43" x2="-12.7" y2="-24.13" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-33.02" x2="2.54" y2="-30.48" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-26.67" x2="2.54" y2="-24.13" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-24.13" x2="-12.7" y2="-24.13" width="0.8128" layer="16"/>
<wire x1="-12.7" y1="-11.43" x2="-15.24" y2="-11.43" width="0.8128" layer="16"/>
<wire x1="-12.7" y1="-6.35" x2="-5.08" y2="-6.35" width="0.8128" layer="16"/>
<wire x1="-5.08" y1="-6.35" x2="-5.08" y2="-16.51" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="-16.51" x2="-7.62" y2="-22.86" width="0.8128" layer="16"/>
<wire x1="13.97" y1="-8.89" x2="11.43" y2="-8.89" width="0.8128" layer="16"/>
<wire x1="11.43" y1="-8.89" x2="11.43" y2="-13.97" width="0.8128" layer="16"/>
<wire x1="11.43" y1="-13.97" x2="12.7" y2="-13.97" width="0.8128" layer="16"/>
<wire x1="12.7" y1="-13.97" x2="12.7" y2="-22.86" width="0.8128" layer="16"/>
<wire x1="12.7" y1="-22.86" x2="-7.62" y2="-22.86" width="0.8128" layer="16"/>
<wire x1="2.54" y1="-24.13" x2="15.24" y2="-24.13" width="0.8128" layer="16"/>
<wire x1="15.24" y1="-24.13" x2="15.24" y2="-11.43" width="0.8128" layer="16"/>
<wire x1="15.24" y1="-11.43" x2="13.97" y2="-11.43" width="0.8128" layer="16"/>
<wire x1="13.97" y1="-6.35" x2="-5.08" y2="-6.35" width="0.8128" layer="16"/>
<wire x1="13.97" y1="-3.81" x2="-5.08" y2="-3.81" width="0.8128" layer="16"/>
<wire x1="-5.08" y1="-3.81" x2="-12.7" y2="-3.81" width="0.8128" layer="16"/>
<wire x1="-5.08" y1="3.81" x2="-5.08" y2="-3.81" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="3.81" x2="-7.62" y2="10.16" width="0.8128" layer="16"/>
<wire x1="-7.62" y1="10.16" x2="12.7" y2="10.16" width="0.8128" layer="16"/>
<wire x1="2.54" y1="11.43" x2="2.54" y2="13.97" width="0.8128" layer="16"/>
<wire x1="13.97" y1="-8.89" x2="16.51" y2="-8.89" width="0.8128" layer="16"/>
<wire x1="16.51" y1="-8.89" x2="16.51" y2="1.27" width="0.8128" layer="16"/>
<wire x1="16.51" y1="1.27" x2="15.24" y2="1.27" width="0.8128" layer="16"/>
<wire x1="15.24" y1="1.27" x2="15.24" y2="7.62" width="0.8128" layer="16"/>
<pad name="VX0" x="15.24" y="15.24" drill="0.8" shape="square"/>
<pad name="GNDX0" x="12.7" y="15.24" drill="0.8" shape="square"/>
<wire x1="12.7" y1="12.7" x2="12.7" y2="15.24" width="0.8128" layer="16"/>
<wire x1="15.24" y1="15.24" x2="15.24" y2="12.7" width="0.8128" layer="16"/>
<wire x1="13.97" y1="-1.27" x2="12.7" y2="-1.27" width="0.8128" layer="16"/>
<wire x1="12.7" y1="-1.27" x2="12.7" y2="7.62" width="0.8128" layer="16"/>
<wire x1="-15.24" y1="-11.43" x2="-15.24" y2="1.27" width="0.8128" layer="16"/>
<wire x1="-15.24" y1="1.27" x2="-10.16" y2="1.27" width="0.8128" layer="16"/>
<wire x1="-10.16" y1="1.27" x2="-10.16" y2="11.43" width="0.8128" layer="16"/>
<wire x1="-10.16" y1="11.43" x2="2.54" y2="11.43" width="0.8128" layer="16"/>
</package>
</packages>
<symbols>
<symbol name="LED_DRIVER_ASSEMBLY_CHIP">
<pin name="VCCIN" x="-20.32" y="-5.08" length="middle"/>
<pin name="SDAIN" x="-20.32" y="0" length="middle"/>
<pin name="SCLIN" x="-20.32" y="25.4" length="middle"/>
<pin name="GNDIN" x="-20.32" y="30.48" length="middle"/>
<rectangle x1="-15.24" y1="-5.08" x2="0" y2="30.48" layer="94"/>
<rectangle x1="-15.24" y1="30.48" x2="0" y2="33.02" layer="94"/>
<rectangle x1="-15.24" y1="-7.62" x2="0" y2="-5.08" layer="94"/>
<pin name="DRAIN1" x="5.08" y="25.4" length="middle" rot="R180"/>
<pin name="DRAIN2" x="5.08" y="20.32" length="middle" rot="R180"/>
<pin name="DRAIN3" x="5.08" y="15.24" length="middle" rot="R180"/>
<pin name="DRAIN4" x="5.08" y="10.16" length="middle" rot="R180"/>
<pin name="DRAIN5" x="5.08" y="5.08" length="middle" rot="R180"/>
<pin name="DRAIN6" x="5.08" y="0" length="middle" rot="R180"/>
<pin name="DRAIN7" x="5.08" y="-5.08" length="middle" rot="R180"/>
<pin name="DRAIN0" x="-20.32" y="5.08" length="middle"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="LED_DRIVER_ASSEMBLY_CHIP">
<gates>
<gate name="G$1" symbol="LED_DRIVER_ASSEMBLY_CHIP" x="7.62" y="-12.7"/>
</gates>
<devices>
<device name="" package="LED_DRIVER_ASSEMBLY_CHIP">
<connects>
<connect gate="G$1" pin="DRAIN0" pad="DRAIN0C"/>
<connect gate="G$1" pin="DRAIN1" pad="DRAIN1C"/>
<connect gate="G$1" pin="DRAIN2" pad="DRAIN2C"/>
<connect gate="G$1" pin="DRAIN3" pad="DRAIN3C"/>
<connect gate="G$1" pin="DRAIN4" pad="DRAIN4C"/>
<connect gate="G$1" pin="DRAIN5" pad="DRAIN5C"/>
<connect gate="G$1" pin="DRAIN6" pad="DRAIN6C"/>
<connect gate="G$1" pin="DRAIN7" pad="DRAIN7C"/>
<connect gate="G$1" pin="GNDIN" pad="GNDC"/>
<connect gate="G$1" pin="SCLIN" pad="SCL"/>
<connect gate="G$1" pin="SDAIN" pad="SDA"/>
<connect gate="G$1" pin="VCCIN" pad="VCC"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$2" library="Parts" deviceset="LED_DRIVER_ASSEMBLY_CHIP" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$2" gate="G$1" x="10.16" y="33.02"/>
</instances>
<busses>
</busses>
<nets>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
