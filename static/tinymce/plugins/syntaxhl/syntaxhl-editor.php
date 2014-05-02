<?php
/**
 * Plugin Name: SyntaxHL Editor
 * Plugin URI: http://www.maclovin.de/syntaxhl-editor
 * Description: Seemless integration of "Syntax Highlighter and Code Colorizer for Wordpress" into TinyMCE
 * Version: 0.1
 * Author: Dennis Frommknecht
 * Author URI: http://www.maclovin.de/
 * 
 * Copyright (C) 2009 Dennis Frommknecht
 */

/**
 * Add SyntaxHL Plugin to TinyMCE
 *
 * @param $init assoc. array of already defined plugins
 * @return $init the changed assoc. array
 */
function tmsh_mce_add_plugins( $init ) {
	$init['syntaxhl'] = WP_PLUGIN_URL.'/syntaxhl-editor/dialog/editor_plugin.js';
	return $init;
}

/**
 * Add SyntaxHL Button to TinyMCE
 *
 * @param $init array of already defined buttons
 * @return $init the changed array
 */
function tmsh_mce_add_buttons( $init ) {
	array_push($init, 'syntaxhl');
	return $init;
}


/**
 * Add class to extended_valid_elements for TinyMCE
 * Not needed anymore??? 
 *
 * @param $init assoc. array of TinyMCE options
 * @return $init the changed assoc. array
 */
function tmsh_mce_valid_elements( $init ) {
    $element = "pre[class]";

//    These are for Google Syntax Highlighter
//    $element = "pre[cols|rows|disabled|name|readonly|class]";

    // Add to extended_valid_elements if it alreay exists
    if ( isset( $init['extended_valid_elements'] ) 
         && ! empty( $init['extended_valid_elements'] ) ) {
        $init['extended_valid_elements'] .= ',' . $element;
     } else {
        $init['extended_valid_elements'] = $element;
     }

    // Super important: return $init!
    return $init;
}

//add_filter('tiny_mce_before_init', 'tmsh_mce_valid_elements');
add_filter('mce_external_plugins', 'tmsh_mce_add_plugins');
add_filter('mce_buttons', 'tmsh_mce_add_buttons');
