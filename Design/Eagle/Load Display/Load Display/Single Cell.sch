<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="6.2">
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
<package name="HDSP-I">
<description>&lt;b&gt;LED DISPLAY&lt;/b&gt;&lt;p&gt;
 12-mm 1 character 7 segment, 2 decimal points</description>
<wire x1="6.35" y1="-9.525" x2="-6.35" y2="-9.525" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-6.604" x2="5.334" y2="-6.604" width="0.3048" layer="51"/>
<wire x1="6.35" y1="9.398" x2="6.35" y2="-9.525" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-9.525" x2="-6.35" y2="9.398" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="9.398" x2="6.35" y2="9.398" width="0.1524" layer="21"/>
<wire x1="4.445" y1="4.826" x2="3.6322" y2="0.2032" width="0.1524" layer="51"/>
<wire x1="2.667" y1="-4.826" x2="1.651" y2="-4.826" width="0.1524" layer="51"/>
<wire x1="1.651" y1="-4.826" x2="2.5146" y2="-0.2032" width="0.1524" layer="51"/>
<wire x1="3.429" y1="4.826" x2="4.445" y2="4.826" width="0.1524" layer="51"/>
<wire x1="3.1242" y1="5.588" x2="2.921" y2="4.572" width="0.1524" layer="51"/>
<wire x1="2.921" y1="4.572" x2="-1.143" y2="4.572" width="0.1524" layer="51"/>
<wire x1="-1.143" y1="4.572" x2="-0.9652" y2="5.588" width="0.1524" layer="51"/>
<wire x1="-0.9652" y1="5.588" x2="3.1242" y2="5.588" width="0.1524" layer="51"/>
<wire x1="-4.3942" y1="-4.8768" x2="-3.556" y2="-0.2286" width="0.1524" layer="51"/>
<wire x1="-2.6162" y1="4.8514" x2="-1.5494" y2="4.8514" width="0.1524" layer="51"/>
<wire x1="-3.3274" y1="-4.8768" x2="-2.4892" y2="-0.2286" width="0.1524" layer="51"/>
<wire x1="-3.3274" y1="-4.8768" x2="-4.3942" y2="-4.8768" width="0.1524" layer="51"/>
<wire x1="1.2446" y1="-4.5974" x2="-2.8194" y2="-4.5974" width="0.1524" layer="51"/>
<wire x1="1.2446" y1="-4.5974" x2="1.0668" y2="-5.6134" width="0.1524" layer="51"/>
<wire x1="-2.9972" y1="-5.6134" x2="-2.8194" y2="-4.5974" width="0.1524" layer="51"/>
<wire x1="1.0668" y1="-5.6134" x2="-2.9972" y2="-5.6134" width="0.1524" layer="51"/>
<wire x1="1.9812" y1="-0.508" x2="-2.0828" y2="-0.508" width="0.1524" layer="51"/>
<wire x1="2.1844" y1="0.508" x2="1.9812" y2="-0.508" width="0.1524" layer="51"/>
<wire x1="-1.8796" y1="0.508" x2="-2.0828" y2="-0.508" width="0.1524" layer="51"/>
<wire x1="2.1844" y1="0.508" x2="-1.8796" y2="0.508" width="0.1524" layer="51"/>
<wire x1="2.5146" y1="-0.2032" x2="3.556" y2="-0.2032" width="0.1524" layer="51"/>
<wire x1="2.5908" y1="0.2032" x2="3.6322" y2="0.2032" width="0.1524" layer="51"/>
<wire x1="2.5908" y1="0.2032" x2="3.429" y2="4.826" width="0.1524" layer="51"/>
<wire x1="3.556" y1="-0.2032" x2="2.667" y2="-4.826" width="0.1524" layer="51"/>
<wire x1="-3.4798" y1="0.2286" x2="-2.3876" y2="0.2286" width="0.1524" layer="51"/>
<wire x1="-3.556" y1="-0.2286" x2="-2.4892" y2="-0.2286" width="0.1524" layer="51"/>
<wire x1="-3.4798" y1="0.2286" x2="-2.6162" y2="4.8514" width="0.1524" layer="51"/>
<wire x1="-2.3876" y1="0.2286" x2="-1.5494" y2="4.8514" width="0.1524" layer="51"/>
<wire x1="1.5748" y1="0" x2="-1.4224" y2="0" width="1.016" layer="51"/>
<wire x1="2.9464" y1="-0.7112" x2="2.2352" y2="-4.3434" width="1.016" layer="51"/>
<wire x1="0.635" y1="-5.1054" x2="-2.3876" y2="-5.1054" width="1.016" layer="51"/>
<wire x1="-3.7846" y1="-4.3688" x2="-3.1242" y2="-0.7366" width="1.016" layer="51"/>
<wire x1="-2.8448" y1="0.7112" x2="-2.1844" y2="4.3688" width="1.016" layer="51"/>
<wire x1="-0.5334" y1="5.08" x2="2.4892" y2="5.08" width="1.016" layer="51"/>
<wire x1="3.8608" y1="4.2926" x2="3.2004" y2="0.6858" width="1.016" layer="51"/>
<wire x1="1.5494" y1="0.381" x2="2.032" y2="0.381" width="0.254" layer="51"/>
<wire x1="2.032" y1="0.381" x2="1.8542" y2="-0.4064" width="0.1524" layer="51"/>
<wire x1="-1.778" y1="0.381" x2="-1.9304" y2="-0.4064" width="0.254" layer="51"/>
<wire x1="-1.9304" y1="-0.4064" x2="-1.7018" y2="-0.4064" width="0.254" layer="51"/>
<wire x1="2.6162" y1="-0.3302" x2="3.429" y2="-0.3302" width="0.254" layer="51"/>
<wire x1="3.429" y1="-0.3302" x2="3.3528" y2="-0.5842" width="0.254" layer="51"/>
<wire x1="3.556" y1="0.3302" x2="2.7178" y2="0.3302" width="0.254" layer="51"/>
<wire x1="2.7178" y1="0.3302" x2="2.794" y2="0.635" width="0.254" layer="51"/>
<wire x1="-2.4638" y1="0.3302" x2="-3.3528" y2="0.3302" width="0.254" layer="51"/>
<wire x1="-3.3528" y1="0.3302" x2="-3.302" y2="0.5334" width="0.254" layer="51"/>
<wire x1="-2.6416" y1="-0.3556" x2="-2.667" y2="-0.635" width="0.254" layer="51"/>
<wire x1="-3.4544" y1="-0.3556" x2="-2.6416" y2="-0.3556" width="0.254" layer="51"/>
<wire x1="-2.5146" y1="4.7244" x2="-1.6764" y2="4.7244" width="0.254" layer="51"/>
<wire x1="-1.6764" y1="4.7244" x2="-1.7272" y2="4.4958" width="0.254" layer="51"/>
<wire x1="-0.8382" y1="5.4864" x2="-0.9906" y2="4.6736" width="0.254" layer="51"/>
<wire x1="-0.9906" y1="4.6736" x2="-0.7874" y2="4.6736" width="0.254" layer="51"/>
<wire x1="2.5908" y1="4.699" x2="2.8194" y2="4.699" width="0.1524" layer="51"/>
<wire x1="2.8194" y1="4.699" x2="2.9718" y2="5.4864" width="0.254" layer="51"/>
<wire x1="2.9718" y1="5.4864" x2="2.667" y2="5.4864" width="0.254" layer="51"/>
<wire x1="3.5052" y1="4.6736" x2="4.318" y2="4.6736" width="0.254" layer="51"/>
<wire x1="4.318" y1="4.6736" x2="4.2672" y2="4.4958" width="0.254" layer="51"/>
<wire x1="2.5908" y1="-4.699" x2="1.7526" y2="-4.699" width="0.254" layer="51"/>
<wire x1="1.7526" y1="-4.699" x2="1.8034" y2="-4.5466" width="0.254" layer="51"/>
<wire x1="0.9652" y1="-5.5118" x2="1.0922" y2="-4.699" width="0.254" layer="51"/>
<wire x1="1.0922" y1="-4.699" x2="0.7874" y2="-4.699" width="0.254" layer="51"/>
<wire x1="-2.7178" y1="-4.699" x2="-2.8448" y2="-5.5118" width="0.254" layer="51"/>
<wire x1="-2.8448" y1="-5.5118" x2="-2.6162" y2="-5.5118" width="0.254" layer="51"/>
<wire x1="-3.3782" y1="-4.5212" x2="-3.429" y2="-4.7498" width="0.254" layer="51"/>
<wire x1="-3.429" y1="-4.7498" x2="-4.2418" y2="-4.7498" width="0.254" layer="51"/>
<wire x1="-4.2418" y1="-4.7498" x2="-4.191" y2="-4.5466" width="0.254" layer="51"/>
<wire x1="-5.207" y1="-6.731" x2="-4.953" y2="-6.731" width="0.3048" layer="51"/>
<circle x="5.207" y="-6.604" radius="0.254" width="0.6096" layer="51"/>
<circle x="-5.207" y="-6.731" radius="0.254" width="0.6096" layer="51"/>
<pad name="1" x="-3.81" y="7.62" drill="0.8128" shape="long"/>
<pad name="2" x="-3.81" y="5.08" drill="0.8128" shape="long"/>
<pad name="3" x="-3.81" y="2.54" drill="0.8128" shape="long"/>
<pad name="6" x="-3.81" y="-5.08" drill="0.8128" shape="long"/>
<pad name="7" x="-3.81" y="-7.62" drill="0.8128" shape="long"/>
<pad name="8" x="3.81" y="-7.62" drill="0.8128" shape="long"/>
<pad name="9" x="3.81" y="-5.08" drill="0.8128" shape="long"/>
<pad name="10" x="3.81" y="-2.54" drill="0.8128" shape="long"/>
<pad name="11" x="3.81" y="0" drill="0.8128" shape="long"/>
<pad name="13" x="3.81" y="5.08" drill="0.8128" shape="long"/>
<pad name="14" x="3.81" y="7.62" drill="0.8128" shape="long"/>
<text x="-6.223" y="9.9822" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-6.223" y="-11.3538" size="1.27" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="4&quot;">
<pad name="P4" x="15.24" y="0" drill="0.8" shape="square"/>
<pad name="P1" x="0" y="0" drill="0.8" shape="square"/>
<pad name="P5" x="20.32" y="0" drill="0.8" shape="square"/>
<pad name="P2" x="5.08" y="0" drill="0.8" shape="square"/>
<pad name="P3" x="10.16" y="0" drill="0.8" shape="square" rot="R180"/>
<pad name="P10" x="0" y="106.934" drill="0.8" shape="square"/>
<pad name="P9" x="5.08" y="106.934" drill="0.8" shape="square"/>
<pad name="P8" x="10.16" y="106.934" drill="0.8" shape="square"/>
<pad name="P7" x="15.24" y="106.934" drill="0.8" shape="square"/>
<pad name="P6" x="20.32" y="106.934" drill="0.8" shape="square"/>
<wire x1="-34.925" y1="-7.62" x2="-34.925" y2="114.3" width="0.127" layer="21"/>
<wire x1="-34.925" y1="-7.62" x2="60.325" y2="-7.62" width="0.127" layer="21"/>
<wire x1="60.325" y1="-7.62" x2="60.325" y2="114.3" width="0.127" layer="21"/>
<wire x1="60.325" y1="114.3" x2="-34.925" y2="114.3" width="0.127" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="HD7-A">
<wire x1="2.794" y1="-3.683" x2="3.048" y2="-3.683" width="0.3048" layer="94"/>
<wire x1="2.3368" y1="3.1242" x2="2.032" y2="2.8194" width="0.254" layer="94"/>
<wire x1="2.032" y1="2.8194" x2="1.6256" y2="0.6096" width="0.254" layer="94"/>
<wire x1="1.6256" y1="0.6096" x2="1.905" y2="0.3302" width="0.254" layer="94"/>
<wire x1="1.905" y1="0.3302" x2="2.159" y2="0.5842" width="0.254" layer="94"/>
<wire x1="2.159" y1="0.5842" x2="2.54" y2="2.921" width="0.254" layer="94"/>
<wire x1="2.54" y1="2.921" x2="2.3368" y2="3.1242" width="0.254" layer="94"/>
<wire x1="2.032" y1="3.429" x2="1.778" y2="3.175" width="0.254" layer="94"/>
<wire x1="1.778" y1="3.175" x2="-0.762" y2="3.175" width="0.254" layer="94"/>
<wire x1="-0.762" y1="3.175" x2="-1.016" y2="3.429" width="0.254" layer="94"/>
<wire x1="-1.016" y1="3.429" x2="-0.762" y2="3.683" width="0.254" layer="94"/>
<wire x1="-0.762" y1="3.683" x2="1.778" y2="3.683" width="0.254" layer="94"/>
<wire x1="1.778" y1="3.683" x2="2.032" y2="3.429" width="0.254" layer="94"/>
<wire x1="-1.3208" y1="3.1242" x2="-1.016" y2="2.8194" width="0.254" layer="94"/>
<wire x1="-1.016" y1="2.8194" x2="-1.397" y2="0.6096" width="0.254" layer="94"/>
<wire x1="-1.397" y1="0.6096" x2="-1.651" y2="0.3556" width="0.254" layer="94"/>
<wire x1="-1.651" y1="0.3556" x2="-1.905" y2="0.6096" width="0.254" layer="94"/>
<wire x1="-1.905" y1="0.6096" x2="-1.524" y2="2.921" width="0.254" layer="94"/>
<wire x1="-1.524" y1="2.921" x2="-1.3208" y2="3.1242" width="0.254" layer="94"/>
<wire x1="-1.4732" y1="-0.0762" x2="-1.143" y2="0.254" width="0.254" layer="94"/>
<wire x1="-1.143" y1="0.254" x2="1.3462" y2="0.254" width="0.254" layer="94"/>
<wire x1="1.3462" y1="0.254" x2="1.5494" y2="0.0508" width="0.254" layer="94"/>
<wire x1="1.5494" y1="0.0508" x2="1.2446" y2="-0.254" width="0.254" layer="94"/>
<wire x1="1.2446" y1="-0.254" x2="-1.2954" y2="-0.254" width="0.254" layer="94"/>
<wire x1="-1.2954" y1="-0.254" x2="-1.4732" y2="-0.0762" width="0.254" layer="94"/>
<wire x1="-1.8288" y1="-0.3302" x2="-1.5748" y2="-0.5842" width="0.254" layer="94"/>
<wire x1="-2.286" y1="-3.1242" x2="-1.9558" y2="-2.794" width="0.254" layer="94"/>
<wire x1="-1.9558" y1="-2.794" x2="-1.5748" y2="-0.5842" width="0.254" layer="94"/>
<wire x1="-1.8288" y1="-0.3302" x2="-2.1082" y2="-0.6096" width="0.254" layer="94"/>
<wire x1="-2.1082" y1="-0.6096" x2="-2.4892" y2="-2.921" width="0.254" layer="94"/>
<wire x1="-2.4892" y1="-2.921" x2="-2.286" y2="-3.1242" width="0.254" layer="94"/>
<wire x1="-1.9812" y1="-3.429" x2="-1.7272" y2="-3.175" width="0.254" layer="94"/>
<wire x1="-1.7272" y1="-3.175" x2="0.8128" y2="-3.175" width="0.254" layer="94"/>
<wire x1="0.8128" y1="-3.175" x2="1.0668" y2="-3.429" width="0.254" layer="94"/>
<wire x1="1.0668" y1="-3.429" x2="0.8128" y2="-3.683" width="0.254" layer="94"/>
<wire x1="0.8128" y1="-3.683" x2="-1.7272" y2="-3.683" width="0.254" layer="94"/>
<wire x1="-1.7272" y1="-3.683" x2="-1.9812" y2="-3.429" width="0.254" layer="94"/>
<wire x1="1.7018" y1="-0.4064" x2="1.4478" y2="-0.6604" width="0.254" layer="94"/>
<wire x1="1.4478" y1="-0.6604" x2="1.0668" y2="-2.8194" width="0.254" layer="94"/>
<wire x1="1.0668" y1="-2.8194" x2="1.3716" y2="-3.1242" width="0.254" layer="94"/>
<wire x1="1.3716" y1="-3.1242" x2="1.5748" y2="-2.921" width="0.254" layer="94"/>
<wire x1="1.5748" y1="-2.921" x2="1.9558" y2="-0.6604" width="0.254" layer="94"/>
<wire x1="1.9558" y1="-0.6604" x2="1.7018" y2="-0.4064" width="0.254" layer="94"/>
<wire x1="2.286" y1="2.794" x2="1.905" y2="0.635" width="0.4064" layer="94"/>
<wire x1="1.778" y1="3.429" x2="-0.762" y2="3.429" width="0.4064" layer="94"/>
<wire x1="-1.27" y1="2.794" x2="-1.651" y2="0.635" width="0.4064" layer="94"/>
<wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.4064" layer="94"/>
<wire x1="1.651" y1="-0.762" x2="1.27" y2="-2.794" width="0.4064" layer="94"/>
<wire x1="0.762" y1="-3.429" x2="-1.651" y2="-3.429" width="0.4064" layer="94"/>
<wire x1="-2.286" y1="-2.921" x2="-1.905" y2="-0.635" width="0.4064" layer="94"/>
<wire x1="-8.89" y1="5.08" x2="8.89" y2="5.08" width="0.4064" layer="94"/>
<wire x1="8.89" y1="-5.08" x2="8.89" y2="5.08" width="0.4064" layer="94"/>
<wire x1="8.89" y1="-5.08" x2="-8.89" y2="-5.08" width="0.4064" layer="94"/>
<wire x1="-8.89" y1="5.08" x2="-8.89" y2="-5.08" width="0.4064" layer="94"/>
<wire x1="7.62" y1="-4.953" x2="7.62" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="5.08" y1="-4.953" x2="5.08" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="0" y1="-4.953" x2="0" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="-5.08" y1="-4.953" x2="-5.08" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="-7.62" y1="-4.953" x2="-7.62" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="7.62" y1="10.16" x2="7.62" y2="4.953" width="0.1524" layer="94"/>
<wire x1="-2.54" y1="-4.953" x2="-2.54" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="2.54" y1="-4.953" x2="2.54" y2="-10.16" width="0.1524" layer="94"/>
<wire x1="-7.62" y1="10.16" x2="-7.62" y2="4.953" width="0.1524" layer="94"/>
<wire x1="5.08" y1="10.16" x2="5.08" y2="4.953" width="0.1524" layer="94"/>
<circle x="2.921" y="-3.683" radius="0.254" width="0.3048" layer="94"/>
<text x="-9.525" y="-5.08" size="1.778" layer="95" rot="R90">&gt;NAME</text>
<text x="11.43" y="-5.08" size="1.778" layer="96" rot="R90">&gt;VALUE</text>
<text x="7.366" y="6.096" size="1.27" layer="95" rot="R90">CA</text>
<text x="4.826" y="6.096" size="1.27" layer="95" rot="R90">CA</text>
<text x="-7.874" y="-7.239" size="1.27" layer="95" rot="R90">a</text>
<text x="-5.334" y="-7.239" size="1.27" layer="95" rot="R90">b</text>
<text x="-2.794" y="-7.239" size="1.27" layer="95" rot="R90">c</text>
<text x="-0.254" y="-7.239" size="1.27" layer="95" rot="R90">d</text>
<text x="2.286" y="-7.239" size="1.27" layer="95" rot="R90">e</text>
<text x="4.826" y="-7.239" size="1.27" layer="95" rot="R90">f</text>
<text x="7.366" y="-7.239" size="1.27" layer="95" rot="R90">g</text>
<text x="-7.874" y="6.096" size="1.27" layer="95" rot="R90">dp</text>
<pin name="DP" x="-7.62" y="15.24" visible="pad" length="middle" direction="pas" rot="R270"/>
<pin name="F" x="5.08" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="D" x="0" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="B" x="-5.08" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="A" x="-7.62" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="CA" x="7.62" y="15.24" visible="pad" length="middle" direction="pas" rot="R270"/>
<pin name="C" x="-2.54" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="E" x="2.54" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="G" x="7.62" y="-15.24" visible="pad" length="middle" direction="pas" rot="R90"/>
<pin name="CA@1" x="5.08" y="15.24" visible="pad" length="middle" direction="pas" rot="R270"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="HD-E101" prefix="DIS">
<description>&lt;b&gt;LED DISPLAY&lt;/b&gt;&lt;p&gt;
 1-character 7 segment, decimal point right</description>
<gates>
<gate name="A" symbol="HD7-A" x="0" y="0"/>
</gates>
<devices>
<device name="" package="HDSP-I">
<connects>
<connect gate="A" pin="A" pad="1"/>
<connect gate="A" pin="B" pad="13"/>
<connect gate="A" pin="C" pad="10"/>
<connect gate="A" pin="CA" pad="3"/>
<connect gate="A" pin="CA@1" pad="14"/>
<connect gate="A" pin="D" pad="8"/>
<connect gate="A" pin="DP" pad="9"/>
<connect gate="A" pin="E" pad="7"/>
<connect gate="A" pin="F" pad="2"/>
<connect gate="A" pin="G" pad="11"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
<device name="LARGE" package="4&quot;">
<connects>
<connect gate="A" pin="A" pad="P7"/>
<connect gate="A" pin="B" pad="P6"/>
<connect gate="A" pin="C" pad="P4"/>
<connect gate="A" pin="CA" pad="P3"/>
<connect gate="A" pin="CA@1" pad="P8"/>
<connect gate="A" pin="D" pad="P2"/>
<connect gate="A" pin="DP" pad="P5"/>
<connect gate="A" pin="E" pad="P1"/>
<connect gate="A" pin="F" pad="P9"/>
<connect gate="A" pin="G" pad="P10"/>
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
<part name="DIS1" library="Parts" deviceset="HD-E101" device="LARGE"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="DIS1" gate="A" x="15.24" y="50.8"/>
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
