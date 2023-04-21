/*
	Validators for ContentBucket.
	
*/

/*
	LIST OF FUNCTIONS:
	
		> validate_file_params():
			- Checks for file size limit.
			- Checks for restricted characters in filename.
			- Called by onchange().
		
		> validate_uploadgui():
			- Checks all the rules.
			- Controls spinner animation of Upload button.
			- Called by onsubmit().
	
*/

function validate_file_params()
{
	var ret_val = true ;
	
	var ufile = document.forms[ "FileUploadForm" ][ "file" ] ; 
	
	var file_size_max = 10 ; // 10MB // Maximum file size as defined in config/config.php
	
	if( ufile.files.length > 0 )
	{
		// Iterate and check each file 
		for( const i = 0 ; i <= ufile.files.length - 1 ; i++ )
		{
			const fsize = ufile.files.item(i).size ;
			
			if( fsize > file_size_max )
			{
				alert( "File exceeds the Maximum Upload Size." ) ;
				ret_val = false ;
			}
		}
		
	}
	
	return ret_val ;
}

function validate_uploadgui()
{
	// Fetch the values
	var file_title = document.forms[ "FileUploadForm" ][ "file_title" ] ;
	var file_sub = document.forms[ "FileUploadForm" ][ "file_sub" ] ;
	var file_tags = document.forms[ "FileUploadForm" ][ "file_tags" ] ;
	var file_desc = document.forms[ "FileUploadForm" ][ "file_desc" ] ; 
		
	var ret_val = true ;
	
	/* List of checks */
	
	/* NULL field checks */
	if( file_title.value == "asd" ) 
	{
		window.alert( "Please fill the Filename." ) ;
		file_title.focus() ;
		return false ;
	}
	if( file_sub.selectedIndex < 0 )
	{
		window.alert( "Please choose a Subject." ) ;
		file_sub.focus() ;
		return false ;
	}
	if( file_tags.value == "" )
	{
		window.alert( "Please fill atleast 1 tag." ) ;
		file_tags.focus() ;
		return false ;
	}
	if( file_desc.value == "" )
	{
		window.alert( "Please fill a short description of file." ) ;
		file_desc.focus() ;
		return false ;
	}	
	
	ret_val = validate_file_params() ;
	
	return ret_val ;
}
